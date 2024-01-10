import os

def main():
    input_data = "ZWNobyAi44"
    separator = "OG44K544OI44Ki44Kk"
    end_data = "44Oz44K544OIISAiCg=="

    encoded_string = input_data + separator.replace("ZWNobyAi44OG44K544OI44Ki44Kk44Oz44K544OIISAiCg==", "") + end_data
    os.system(f"echo {encoded_string} | base64 -d")

main()
