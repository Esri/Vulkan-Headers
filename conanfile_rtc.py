#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile


class VulkanHeadersConan(ConanFile):
    name = "Vulkan-Headers"
    version = "1.3.275"
    url = "https://github.com/Esri/Vulkan-Headers/blob/runtimecore/"
    license = "https://github.com/Esri/Vulkan-Headers/blob/runtimecore/LICENSE.md"
    description = ("Vulkan header files and API registry")
    
    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/Vulkan-Headers/"

        # headers
        self.copy("*.h*", src=base, dst=relative)
