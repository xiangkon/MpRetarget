from utils.smpl import load_smplx_file, get_smplx_data_offline_fast

smplx_file = "/home/hdh/project/GMR/data/walkdog_stageii.npz"
SMPLX_FOLDER = "/home/hdh/project/GMR/assets/body_models"
tgt_fps = 30

# Load SMPLX trajectory
smplx_data, body_model, smplx_output, actual_human_height = load_smplx_file(
    smplx_file, SMPLX_FOLDER
)

smplx_data_frames, aligned_fps = get_smplx_data_offline_fast(smplx_data, body_model, smplx_output, tgt_fps=tgt_fps)

print(len(smplx_data_frames[0])) # 21(body) + 30(hand) + 2(eye) + 1(jaw) + 1(base) 