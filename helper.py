# Re-import necessary libraries after code execution state reset
import pandas as pd
import numpy as np

def generate_data(n_samples, seed=42):
    np.random.seed(seed)
    # Initialize data dictionary
    data_conditional = {
        "ID Anak": range(1, n_samples + 1),
        "Risiko Stunting": np.random.choice([0, 1], size=n_samples)  # Random stunting risk label
    }

    # Define ranges for conditional data based on 'Risiko Stunting'
    data_conditional["Usia (bulan)"] = np.random.randint(6, 60, size=n_samples)

    # Assign weight and height ranges as reasonable values based on age
    data_conditional["Berat Badan (kg)"] = np.where(data_conditional["Risiko Stunting"] == 0,
                                                    np.round(np.random.uniform(10, 18, size=n_samples), 1),
                                                    np.round(np.random.uniform(7, 13, size=n_samples), 1))

    data_conditional["Tinggi Badan (cm)"] = np.where(data_conditional["Risiko Stunting"] == 0,
                                                    np.round(np.random.uniform(80, 110, size=n_samples), 1),
                                                    np.round(np.random.uniform(65, 85, size=n_samples), 1))

    data_conditional["Asupan Gizi (Kcal/hari)"] = np.where(data_conditional["Risiko Stunting"] == 0,
                                                        np.random.randint(1300, 1600, size=n_samples),
                                                        np.random.randint(900, 1200, size=n_samples))

    data_conditional["Kualitas Air (%)"] = np.where(data_conditional["Risiko Stunting"] == 0,
                                                    np.random.randint(85, 100, size=n_samples),
                                                    np.random.randint(60, 85, size=n_samples))

    data_conditional["Status Ekonomi"] = np.where(data_conditional["Risiko Stunting"] == 0,
                                                np.random.choice([2, 3], size=n_samples),  # Better economic status
                                                np.random.choice([1, 2], size=n_samples))  # Lower economic status

    data_conditional["Akses Fasilitas Kesehatan"] = np.where(data_conditional["Risiko Stunting"] == 0,
                                                            1,  # Good healthcare access
                                                            np.random.choice([0, 1], size=n_samples))

    data_conditional["Riwayat Kesehatan"] = np.where(data_conditional["Risiko Stunting"] == 0,
                                                    1,  # Good health history
                                                    np.random.choice([0, 1], size=n_samples))

    # Convert the data dictionary to a DataFrame
    df_dummy_data_conditional = pd.DataFrame(data_conditional)

    # Display the first few rows of the new dummy data
    return df_dummy_data_conditional
