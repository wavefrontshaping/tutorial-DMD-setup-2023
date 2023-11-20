import pickle

DATA_FILE = "./data_correction_Zernike_big"
NEW_DATA_FILE = "./data_correction_Zernike"

with open(DATA_FILE, "rb") as file:
    data = pickle.load(file)

new_data = {
    "final_last_image": data["final_last_image"],
    "zernike_coefficients": data["zernike_coefficients"],
    "correction_complex_mask": data["correction_complex_mask"],
    "evol_coeff_imgs": data["evol_coeff_imgs"],
}
data = new_data

pickle.dump(data, open(NEW_DATA_FILE, "wb"))
