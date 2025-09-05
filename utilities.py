import yaml
import json
import shutil
import os


def read_config():
    """Read config file"""
    dic = ""
    with open("config.yaml", "r") as stream:
        try:
            dic = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dic


def validate_path(company_path):
    """Validate Path"""
    response = False
    if os.path.exists(company_path):
        response = True
    else:
        response = False
    return response


def create_requirement(company_path, require_name):
    """Create requirement"""

    new_dir = company_path + '\\' + require_name
    print(f"newdir {new_dir}")
    print(validate_path(new_dir))
    if validate_path(new_dir):
        print(f"El requerimiento {require_name} ya existe")
    else:
        try:
            os.mkdir(new_dir)
            print(f"Carpeta '{require_name}' creada con éxito. ✅")
        except FileExistsError:
            print(f"La carpeta '{require_name}' ya existe. ⚠️")
        except OSError as error:
            print(f"Error al crear la carpeta: {error} ❌")


def create_other_dir(company_path, require_name):
    new_dir = company_path + '\\' + require_name
    """Create Other Dir"""
    dic = read_config()
    print(dic)
    documents = dic['path']['documents']
    repository = dic['path']['repository']
    workspace = dic['path']['workspace']
    tmforum = dic['path']['tmforum']
    release = dic['path']['release']
    try:
        os.mkdir(new_dir + '\\' + documents)
        os.mkdir(new_dir + '\\' + repository)
        os.mkdir(new_dir + '\\' + workspace)
        os.mkdir(new_dir + '\\' + tmforum)
        os.mkdir(new_dir + '\\' + release)
        print(f"Conjunto de carpetas creadas con éxito. ✅")
    except FileExistsError:
        print(f"La carpeta '{require_name}' ya existe. ⚠️")
    except OSError as error:
        print(f"Error al crear la carpeta: {error} ❌")


def add_templates(ori_path, destination_path):
    """Copy Templates"""
    try:
        shutil.copy(ori_path, destination_path)
    except FileNotFoundError:
        print("❌ Error: El archivo de origen o el directorio de destino no se encontró.")
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")


def prueba(company_path, require_name):
    """Prueba"""
    destination_path = company_path + '\\' + require_name
    dic = read_config()
    print(dic)
    documents = dic['path']['documents']
    release = dic['path']['release']
    try:
        shutil.copy('./template/credenciales.txt',
                    destination_path + '\\' + documents + '\\' + 'credenciales.txt')
        shutil.copy('./template/credenciales.txt',
                    destination_path + '\\' + documents + '\\' + 'template_hoja_de_vida_api.md')
        shutil.copy('./template/Cronograma.xlsx',
                    destination_path + '\\' + documents + '\\' + 'Cronograma.xlsx')
        shutil.copy('./template/Estimacion.txt',
                    destination_path + '\\' + documents + '\\' + 'Estimacion.txt')
        shutil.copy('./template/ManualDespliegue.txt',
                    destination_path + '\\' + release + '\\' + 'ManualDespliegue.txt')
        shutil.copy('./template/DISEÑO DE CASOS DE PRUEBA.xlsx',
                    destination_path + '\\' + release + '\\' + 'DISEÑO DE CASOS DE PRUEBA.xlsx')
        print(f"Conjunto de templates creados con éxito. ✅")
    except FileExistsError:
        print(f"Error al crear archivo. ⚠️")
    except OSError as error:
        print(f"Error al crear la carpeta: {error} ❌")
