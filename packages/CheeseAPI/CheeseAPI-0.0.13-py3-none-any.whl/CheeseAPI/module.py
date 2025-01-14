import os, traceback, inspect, pkg_resources
from typing import Set

import CheeseLog

class Module:
    def __init__(self, modules, name: str):
        self.name: str = name
        self.subModules: Set[str] = set()

        try:
            mainModule = __import__(name)
            self.version: str = pkg_resources.get_distribution(self.name).version
        except:
            CheeseLog.error(f'The error occured while the module \'{name}\' loading\n{traceback.format_exc()}'[:-1])
            raise SystemExit()

        dependencies = None
        try:
            dependencies = mainModule.CheeseAPI_module_dependencies
        except:
            ...
        if dependencies:
            for dependency in dependencies:
                if modules not in modules:
                    modules.add(Module(modules, dependency))

        modulePath = os.path.dirname(inspect.getfile(mainModule))

        if not hasattr(mainModule, 'CheeseAPI_module_type'):
            CheeseLog.error(f'The error occured while the module \'{name}\' loading:\nUnknown module type')
            raise SystemExit()

        if mainModule.CheeseAPI_module_type == 'single':
            for filename in os.listdir(modulePath):
                filePath = os.path.join(modulePath, filename)
                if os.path.isfile(filePath) and filename != '__init__.py':
                    filename = filename[:-3]
                    try:
                        module = __import__(f'{self.name}.{filename}')
                    except:
                        CheeseLog.error(f'The error occured while the module \'{name}\' loading:\n{traceback.format_exc()}'[:-1])
                        raise SystemExit()

                    self.subModules.add(module)
        elif mainModule.CheeseAPI_module_type == 'multiple':
            for foldername in os.listdir(modulePath):
                if foldername == '__pycache__':
                    continue
                folderPath = os.path.join(modulePath, foldername)
                if os.path.isdir(folderPath):
                    for filename in os.listdir(folderPath):
                        filePath = os.path.join(folderPath, filename)
                        if os.path.isfile(filePath) and filename != '__init__.py':
                            filename = filename[:-3]
                            try:
                                module = __import__(f'{self.name}.{foldername}.{filename}')
                            except:
                                CheeseLog.error(f'The error occured while the module \'{name}\' loading:\n{traceback.format_exc()}'[:-1])
                                raise SystemExit()
        else:
            CheeseLog.error(f'The error occured while the module \'{name}\' loading:\nUnknown module type')
            raise SystemExit()

class LocalModule:
    def __init__(self, basePath: str, name: str):
        self.name: str = name
        self.subModules: Set[str] = set()

        modulePath = os.path.join(basePath, name)
        if not os.path.isdir(modulePath):
            raise ImportError(f'could not find module \'{name}\'')

        for filename in os.listdir(modulePath):
            filePath = os.path.join(modulePath, filename)
            if os.path.isfile(filePath) and filename != '__init__.py':
                filename = filename[:-3]
                try:
                    module = __import__(f'{self.name}.{filename}')
                except:
                    CheeseLog.error(f'The error occured while the local module \'{name}\' loading:\n{traceback.format_exc()}'[:-1])
                    raise SystemExit()
                self.subModules.add(module)
