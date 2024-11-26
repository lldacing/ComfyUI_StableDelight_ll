# import os
#
# import folder_paths
#
# models_dir_key = "ben"
# models_dir_default = os.path.join(folder_paths.models_dir, "rembg/ben")
#
# if not os.path.exists(models_dir_default):
#     os.makedirs(models_dir_default, exist_ok=True)
#
# if models_dir_key not in folder_paths.folder_names_and_paths:
#     folder_paths.folder_names_and_paths[models_dir_key] = (
#         [models_dir_default], folder_paths.supported_pt_extensions)
# else:
#     folder_paths.add_model_folder_path(models_dir_key, models_dir_default)
