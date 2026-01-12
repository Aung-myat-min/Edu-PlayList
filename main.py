from controllers.state_controller import load_program_state, save_program_state
from controllers.app_flow_controller import run_login_flow, run_app_loop

def main():
    # 1. Login
    if not run_login_flow():
        return

    # 2. Load Data
    program_state = load_program_state()

    # 3. Run App
    try:
        run_app_loop(program_state)
    except KeyboardInterrupt:
        print("\n⚠️ Program interrupted. Saving state and exiting...")
        save_program_state(program_state)
    except Exception as e:
        print(f"❌ Critical Error: {e}")
        # Try to save if possible
        if 'program_state' in locals():
            save_program_state(program_state)

if __name__ == "__main__":
    main()
