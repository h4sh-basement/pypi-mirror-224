import os
import subprocess
import shutil
from pathlib import Path
import regis.diagnostics
import regis.rex_json

settingsPathFromRoot = os.path.join("_build", "config", "settings.json")

def create_version_file(directory : str, tag : str):
    version = {
        "tag": tag
    }

    path = os.path.join(directory, "version.json")
    regis.rex_json.save_file(path, version)

def load_version_file(directory):
  version_file = os.path.join(directory, "version.json")
  if os.path.exists(version_file):
    version_data = regis.rex_json.load_file(version_file)           
    if version_data != None:
      return version_data["tag"]

  return ''

def env_paths():
  envPath = os.environ["PATH"]
  paths = envPath.split(os.pathsep)
  return paths

def retrieve_header_filters(targetDir, projectName):
  filepath = os.path.join(targetDir, f"{projectName}.project")

  if not os.path.exists(filepath):
    raise Exception(f"clang tools project file doesn't exist, please check your sharpmake scripts: {filepath}")

  jsonBlob = regis.rex_json.load_file(filepath)
  return jsonBlob["HeaderFilters"]

def create_header_filter_regex(headerFilters : list[str]):
  res = ""

  for filter in headerFilters:
    res += "("
    res += filter
    res += ")|"

  res = res.removesuffix("|")
  return res

def find_file_in_folder(file, path : str):
  fileToFind = file.lower()
  subFilesOrFolders = os.listdir(path)
  for fileOrFolder in subFilesOrFolders:
    absPath = os.path.join(path, fileOrFolder)
    if os.path.isfile(absPath):
      file_name = Path(absPath).name.lower()
      if file_name == fileToFind:
        return absPath
  
  return ''

def find_file_in_paths(file, directories : list[str]):
  for path in directories:
    if not os.path.exists(path):
      continue

    result = find_file_in_folder(file, path)
    if result != '':
      return result

  return ''

def find_directory_in_paths(dir : str, directories : list[str]):
  dir = dir.replace('\\', '/')
  folders = dir.split('/')  
  num_folders = len(folders)

  for path in directories:
    path = path.replace('\\', '/')
    path_folders = path.split('/')

    dir_idx = -1

    if os.path.exists(os.path.join(path, dir)):
      return os.path.join(path, dir)

    dir_idx = num_folders - 1
    path_idx = len(path_folders) - 1
    if (len(path_folders) < num_folders):
      continue

    while dir_idx >= 0:
      dir_folder = folders[dir_idx]
      path_folder = path_folders[path_idx]
      
      if dir_folder != path_folder:
        break

      dir_idx -= 1
      path_idx -= 1

    if dir_idx == -1:
      if os.path.exists(path):
        return path
      else:
        diagnostics.log_err(f"matching directory found, but doesn't exist: {path}")

  return None

def find_in_parent(path, toFind):
  curr_path = path

  while toFind not in os.listdir(curr_path):
    if Path(curr_path).parent == curr_path:
      diagnostics.log_err(f"{toFind} not found in parents of {path}")
      return ''

    curr_path = Path(curr_path).parent

  return curr_path

def find_root():
  res = find_in_parent(os.getcwd(), "source")
  if (res == ''):
    regis.diagnostics.log_err(f"root not found")

  return res

def find_files_with_extension(path : str, extension : str):
  files = os.listdir(path)
  files_with_extension = []
  for file in files:
    if Path(file).suffix == extension:
      files_with_extension.append(file)

  return files_with_extension

def is_windows():
  return os.name == 'nt'

def run_subprocess(command):
  proc = subprocess.Popen(command)
  return proc

def run_and_get_output(command):
  proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, errc = proc.communicate()

  return output.decode('utf-8'), proc.returncode

def run_subprocess_with_working_dir(command, workingDir):
  proc = subprocess.Popen(command, cwd=workingDir)
  return proc

def run_subprocess_with_callback(command, callback, filterLines):
  proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  callback(proc.pid, proc.stdout, False, filterLines)
  callback(proc.pid, proc.stderr, True, filterLines)
  return proc

def wait_for_process(process):
  streamdata = process.communicate()[0]
  return process.returncode  

def is_executable(path):
  if is_windows():
    if Path(path).suffix == ".exe":
      return True
  else:
    return os.access(path, os.X_OK)

def find_all_files_in_folder(dir, toFindRegex):
  return list(Path(dir).rglob(toFindRegex))

def remove_folders_recursive(dir : str):
  if os.path.exists(dir):
    shutil.rmtree(dir)