def extract_feature(target_file_path: str):
    features = ['network', 'process']
    for feature in features:
        if feature not in target_file_path:
            continue
        return feature
