#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys


filename = "add_item.json"
""" saved as a JSON representation in a file named add_item.json """
save_to_json_file(sys.argv[1:], filename)
load_from_json_file(filename)
