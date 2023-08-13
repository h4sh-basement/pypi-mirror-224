import os
import sys
import shutil
import platform

from pitrix.constants.constants import Conf
from pitrix.database.sqlite import SQLiteDB
from pitrix.constants.constants import DataBase as DB
from pitrix.utils.log import log


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        log.info(f"创建文件夹: {path}")

def create_file(path, file_content=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(file_content)
    log.info(f"创建文件: {path}")

def delete_folder(path):
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
        log.info(f"删除目录:{path} 成功")
    else:
        log.info(f"{path} 未找到,请手动删除项目")

def create_scaffold(project_name):
    if os.path.isdir(project_name):
        log.warning(f"项目文件夹 {project_name} 已存在，请指定新的项目名称.")
        sys.exit(1)
    elif os.path.isfile(project_name):
        log.warning(f"工程名称 {project_name} 与已存在的文件冲突，请指定一个新的文件.")
        sys.exit(1)

    def create_table(db_object, table_name: str):
        table_attr = get_table_attribute(table_name)
        key = table_attr.get('key')
        value = table_attr.get('value')
        worker = table_attr.get('worker')
        api_info = table_attr.get('api_info')
        if worker is not None:
            sql = f"""create table {table_name}({key} text,{value} text,{worker} text,{api_info} text);"""
        else:
            sql = f"""create table {table_name}({key} text,{value} text);"""
        db_object.execute_sql(sql)
        if table_name != "cache":
            sql2 = f"""create unique index {table_name}_{key}_uindex on {table_name} ({key});"""
            db_object.execute_sql(sql2)
        log.debug(f"创建数据表：{table_name}")

    def get_table_attribute(table_name: str):
        tables_attr = {
            DB.CACHE_TABLE: {'key': DB.CACHE_VAR_NAME, 'value': DB.CACHE_RESPONSE, 'worker': DB.CACHE_WORKER},
            DB.CONFIG_TABLE: {'key': DB.CONFIG_KEY, 'value': DB.CONFIG_VALUE},
            DB.SCHEMA_TABLE: {'key': DB.SCHEMA_API_NAME, 'value': DB.SCHEMA_SCHEMA}
        }
        return tables_attr.get(table_name)

    log.info("🏗🏗🏗 开始创建脚手架 🏗🏗🏗 ")
    log.info(f"创建新项目:【{project_name}】")
    log.info(f"项目根目录: {os.path.join(os.getcwd(), project_name)}")

    create_folder(project_name)

    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

    log.info(f"模版路径:{template_path}")

    for root, dirs, files in os.walk(template_path):
        relative_path = root.replace(template_path, "").lstrip("\\").lstrip("/")
        print("relative_path: {}".format(relative_path))
        if dirs:
            for dir_ in dirs:
                create_folder(os.path.join(project_name, relative_path, dir_))
        if files:
            for file in files:
                with open(os.path.join(root, file), encoding="utf-8") as f:
                    create_file(os.path.join(project_name, relative_path, file.rstrip(Conf.TEMPLATE_SUFFIX)), f.read())

    db_dir_path = os.path.join(project_name, "database")
    db_file_path = os.path.join(db_dir_path, DB.DB_NAME)

    create_folder(db_dir_path)

    db = SQLiteDB(db_path=db_file_path)
    create_table(db, DB.CONFIG_TABLE)
    create_table(db, DB.CACHE_TABLE)
    create_table(db, DB.SCHEMA_TABLE)

    log.info("😄😄😄 脚手架创建完成 😄😄😄 ")

    return True

def create_virtual_environment(project_name):
    os.chdir(project_name)
    log.info("🛠🛠🛠  开始创建虚拟环境 🛠🛠🛠 ")
    os.system("python -m venv .venv")
    log.info("创建虚拟环境: .venv")
    log.info("😄😄😄  虚拟环境创建完成 😄😄😄 ")

    log.info("⏳ ⏳ ⏳  开始安装 pitrix ⏳ ⏳ ⏳ ")
    if platform.system().lower() == 'windows':
        os.chdir(".venv")
        os.chdir("Scripts")
        os.system("pip3 install pitrix")
    elif platform.system().lower() in ['linux','darwin']:
        os.chdir(".venv")
        os.chdir("bin")
        os.system("pip3 install pitrix")
    else:
        raise ValueError("暂不支持此平台")
    log.info("😄😄😄  pitrix安装完成 😄😄😄 ")