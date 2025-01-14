import asyncio
import concurrent.futures
import functools
import glob
import json
import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

from . import network_requests

EXPIRY_TIME_FORMAT = "%Y/%m/%d, %H:%M:%S"
METADATA_FILENAME = "metadata.json"

FILE_EXT = [
    "gpml",
    "gpmlz",
    "gpml.gz",
    "dat",
    "pla",
    "shp",
    "geojson",
    "json",
    ".gpkg",
    "gmt",
    "vgp",
]


class PlateModel:
    """Class to manage a plate model"""

    def __init__(self, model_name: str, model_cfg=None, data_dir=None, readonly=False):
        """Constructor

        :param model_name: model name
        :param model_cfg: model configuration in JSON format
        :param data_dir: the folder path of the model data
        :param readonly: this will return whatever local folder has. Will not attempt to download data from internet

        """
        self.model_name = model_name.lower()
        self.meta_filename = METADATA_FILENAME
        self.expiry_format = EXPIRY_TIME_FORMAT
        self.model = model_cfg
        self.readonly = readonly

        if not data_dir:
            self.data_dir = f"./"
        else:
            self.data_dir = data_dir

        self.model_dir = f"{self.data_dir}/{model_name}/"

        if readonly:
            if not PlateModel.is_model_dir(self.model_dir):
                raise Exception(
                    f"{self.model_dir} must be valid model dir in readonly mode."
                )
            else:
                with open(f"{self.model_dir}/.metadata.json", "r") as f:
                    self.model = json.load(f)

        if not readonly:
            # async and concurrent things
            self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=15)
            self.loop = asyncio.new_event_loop()
            self.run = functools.partial(self.loop.run_in_executor, self.executor)
            asyncio.set_event_loop(self.loop)

    def __del__(self):
        if not self.readonly:
            self.loop.close()

    def get_model_dir(self):
        return self.create_model_dir()

    def get_data_dir(self):
        return self.data_dir

    def set_data_dir(self, new_dir):
        self.data_dir = new_dir
        self.model_dir = f"{self.data_dir}/{self.model_name}/"

    def get_avail_layers(self):
        """get all available layers in this plate model"""
        if not self.model:
            raise Exception("Fatal: No model configuration found!")
        return list(self.model["Layers"].keys())

    def get_rotation_model(self):
        """return a pygplates.RotationModel object"""
        if not self.readonly:
            rotation_folder = self.download_layer_files("Rotations")
        else:
            rotation_folder = f"{self.model_dir}/Rotations"
        rotation_files = glob.glob(f"{rotation_folder}/*.rot")
        rotation_files.extend(glob.glob(f"{rotation_folder}/*.grot"))
        # print(rotation_files)
        return rotation_files

    def get_coastlines(self):
        """return coastlines feature collection"""
        return self.get_layer("Coastlines")

    def get_static_polygons(self):
        """return StaticPolygons feature collection"""
        return self.get_layer("StaticPolygons")

    def get_continental_polygons(self):
        """return ContinentalPolygons feature collection"""
        return self.get_layer("ContinentalPolygons")

    def get_topologies(self):
        """return Topologies feature collection"""
        return self.get_layer("Topologies")

    def get_COBs(self):
        """return COBs feature collection"""
        return self.get_layer("COBs")

    def get_layer(self, layer_name):
        """get layer files by name

        :param layer_name: layer name

        :returns: a list of file names

        """
        if not self.readonly:
            layer_folder = self.download_layer_files(layer_name)
        else:
            layer_folder = f"{self.model_dir}/{layer_name}"
        files = []
        for ext in FILE_EXT:
            files.extend(glob.glob(f"{layer_folder}/*.{ext}"))

        return files

    def create_model_dir(self):
        """create a model folder with a .metadata.json file in it"""
        if self.readonly:
            raise Exception("Unable to create model dir in readonly mode.")
        if not self.model_dir:
            raise Exception(f"Error: model dir is {self.model_dir}")

        # model dir already exists
        if PlateModel.is_model_dir(self.model_dir):
            return self.model_dir

        model_path = self.model_dir
        if os.path.isfile(model_path):
            raise Exception(
                f"Fatal: the model folder {model_path} already exists and is a file!! Remove the file or use another path."
            )

        Path(model_path).mkdir(parents=True, exist_ok=True)

        metadata_file = f"{model_path}/.metadata.json"
        if not os.path.isfile(metadata_file):
            with open(metadata_file, "w+") as f:
                json.dump(self.model, f)

        return model_path

    @staticmethod
    def is_model_dir(folder_path):
        """return True if it is a model dir, otherwise False"""
        return os.path.isdir(folder_path) and os.path.isfile(
            f"{folder_path}/.metadata.json"
        )

    def purge(self):
        """remove the model folder and everything inside it"""
        if os.path.isdir(self.model_dir):
            shutil.rmtree(self.model_dir)

    def purge_layer(self, layer_name):
        """remove the layer folder of the given layer name"""
        layer_path = f"{self.model_dir}/{layer_name}"
        if os.path.isdir(layer_path):
            shutil.rmtree(layer_path)

    def purge_time_dependent_rasters(self, raster_name):
        """remove the raster folder of the given raster name"""
        raster_path = f"{self.model_dir}/{raster_name}"
        if os.path.isdir(raster_path):
            shutil.rmtree(raster_path)

    def download_layer_files(self, layer_name):
        """given the layer name, download the layer files.
        The layer files are in a .zip file. download and unzip it.

        :param layer_name: such as "Rotations","Coastlines", "StaticPolygons", "ContinentalPolygons", "Topologies", etc

        :returns: the folder path which contains the layer files

        """
        if self.readonly:
            raise Exception("Unable to download layer files in readonly mode.")

        print(f"downloading {layer_name}")
        download_flag = False
        meta_etag = None

        # find layer file url. two parts. one is the rotation, the other is all other geometry layers
        if layer_name in self.model:
            layer_file_url = self.model[layer_name]
        elif "Layers" in self.model and layer_name in self.model["Layers"]:
            layer_file_url = self.model["Layers"][layer_name]
        else:
            raise Exception(f"Fatal: No {layer_name} files in configuration file!")

        now = datetime.now()

        model_folder = self.create_model_dir()

        layer_folder = f"{model_folder}/{layer_name}"

        # first check if the layer folder exists
        if os.path.isdir(layer_folder):
            metadata_file = f"{layer_folder}/{self.meta_filename}"
            download_flag, meta_etag = self._check_redownload_need(
                metadata_file, layer_file_url
            )
        else:
            # if the layer folder does not exist
            download_flag = True

        if not download_flag:
            print("The local files are still good. Will not download again.")
        else:
            new_etag = network_requests.fetch_file(
                layer_file_url,
                model_folder,
                etag=meta_etag,
                auto_unzip=True,
            )

            if new_etag != meta_etag:
                # save metadata
                metadata = {
                    "layer_name": layer_name,
                    "url": layer_file_url,
                    "expiry": (now + timedelta(hours=12)).strftime(self.expiry_format),
                    "etag": new_etag,
                }
                with open(f"{layer_folder}/{self.meta_filename}", "w+") as f:
                    json.dump(metadata, f)

        return layer_folder

    def download_all_layers(self):
        """download all layers. Call download_layer_files() on every layer"""
        if self.readonly:
            raise Exception("Unable to download all layers in readonly mode.")

        async def f():
            tasks = []
            if "Rotations" in self.model:
                tasks.append(self.run(self.download_layer_files, "Rotations"))
            if "Layers" in self.model:
                for layer in self.model["Layers"]:
                    tasks.append(self.run(self.download_layer_files, layer))

            # print(tasks)
            await asyncio.wait(tasks)

        self.loop.run_until_complete(f())

    def _check_redownload_need(self, metadata_file, url):
        """check the metadata file and decide if redownload is necessary

        :param metadata_file: metadata file path
        :param url: url for the target file

        :returns download_flag, etag: a flag indicates if redownload is neccesarry and old etag if needed.
        """
        download_flag = False
        meta_etag = None
        if os.path.isfile(metadata_file):
            with open(metadata_file, "r") as f:
                meta = json.load(f)
                if "url" in meta:
                    meta_url = meta["url"]
                    if meta_url != url:
                        # if the data url has changed, re-download
                        download_flag = True
                else:
                    download_flag = True

                # if the url is the same, now check the expiry date
                if not download_flag:
                    if "expiry" in meta:
                        try:
                            meta_expiry = meta["expiry"]
                            expiry_date = datetime.strptime(
                                meta_expiry, self.expiry_format
                            )
                            now = datetime.now()
                            if now > expiry_date:
                                download_flag = True  # expired
                        except ValueError:
                            download_flag = True  # invalid expiry date
                    else:
                        download_flag = True  # no expiry date in metafile

                    if download_flag and "etag" in meta:
                        meta_etag = meta["etag"]
        else:
            download_flag = True  # if metadata_file does not exist

        return download_flag, meta_etag

    def get_avail_time_dependent_raster_names(self):
        """return the names of all time dependent rasters which have been configurated in this model."""
        if not "TimeDepRasters" in self.model:
            return []
        else:
            return [name for name in self.model["TimeDepRasters"]]

    def download_time_dependent_rasters(self, raster_name, times=None):
        """download time dependent rasters, such agegrids

        :param raster_name: raster name, such as AgeGrids. see the models.json
        :param times: if not given, download from begin to end with 1My interval
        """
        if self.readonly:
            raise Exception(
                "Unable to download time dependent rasters in readonly mode."
            )

        if (
            "TimeDepRasters" in self.model
            and raster_name in self.model["TimeDepRasters"]
        ):

            async def f():
                nonlocal times
                tasks = []

                dst_path = f"{self.get_model_dir()}/{raster_name}"
                if not times:
                    times = range(self.model["SmallTime"], self.model["BigTime"])
                for time in times:
                    tasks.append(
                        self.run(
                            self.download_raster,
                            self.model["TimeDepRasters"][raster_name].format(time),
                            dst_path,
                        )
                    )

                # print(tasks)
                await asyncio.wait(tasks)

            self.loop.run_until_complete(f())

        else:
            raise Exception(
                f"Unable to find {raster_name} configuration in this model {self.model_name}."
            )

    def download_raster(self, url, dst_path):
        """download a single raster file from "url" and save the file in "dst_path"
        a metadata file will also be created for the raster file in folder f"{dst_path}/metadata"

        :param url: the url to the raster file
        :param dst_path: the folder path to save the raster file

        """
        if self.readonly:
            raise Exception("Unable to download raster in readonly mode.")
        print(f"downloading {url}")
        filename = url.split("/")[-1]
        metadata_folder = f"{dst_path}/metadata"
        metadata_file = f"{metadata_folder}/{filename}.json"
        download_flag, etag = self._check_redownload_need(metadata_file, url)
        # only redownload when necessary
        if download_flag:
            new_etag = network_requests.fetch_file(
                url,
                dst_path,
                etag=etag,
                auto_unzip=True,
            )
            if etag != new_etag:
                # save metadata file
                metadata = {
                    "url": url,
                    "expiry": (datetime.now() + timedelta(hours=12)).strftime(
                        self.expiry_format
                    ),
                    "etag": new_etag,
                }
                Path(metadata_folder).mkdir(parents=True, exist_ok=True)
                with open(metadata_file, "w+") as f:
                    json.dump(metadata, f)

    def download_all(self):
        """download everything in this plate model"""
        if self.readonly:
            raise Exception("Unable to download all in readonly mode.")
        self.download_all_layers()
        if "TimeDepRasters" in self.model:
            for raster in self.model["TimeDepRasters"]:
                self.download_time_dependent_rasters(raster)
