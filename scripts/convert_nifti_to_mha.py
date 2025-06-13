## Use this script to convert your nifti files to mha to debug I/O of your algorithm

import SimpleITK as sitk

input = "/nfs2/harmonization/BIDS/MASiVar/derivatives/sub-cIVs044/ses-s1Bx1/PreQual/PREPROCESSED/dwmri.nii.gz"
output = "/home-local/lij112/codes/beyond_fa_challenge/dataset/sub-cIVs044_ses-s1Bx1_pq_dwmri.mha"


# Convert NIfTI to MHA
def convert_nifti_to_mha(input_file, output_file):
    image = sitk.ReadImage(input_file)
    sitk.WriteImage(image, output_file)


# Example usage
convert_nifti_to_mha(input, output)
