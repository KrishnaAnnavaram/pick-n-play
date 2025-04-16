# 🎲 Pick-n-Play

**Pick-n-Play** is a Streamlit-powered smart group selector app designed to randomly pick student project groups from an uploaded Excel file — **without repetition**.

### ✨ Features

- ✅ Upload an Excel file with group information
- ✅ Randomly pick one group at a time
- ✅ Prevent duplicate selections (non-repeating logic)
- ✅ Exclude any groups before starting
- ✅ Track completed and excluded groups
- ✅ Simple reset functionality

---

### 📁 Excel Format

The uploaded `.xlsx` file should have the following columns:

| Group   | Student Name            | Project Idea                            |
|---------|--------------------------|------------------------------------------|
| Group 1 | Krishna Annavaram       | Smart Healthcare Assistant               |
|         | Charmika Sadhula        |                                          |
|         | Vighnasree Vara         |                                          |
| Group 2 | John Smith              | AI Weather Forecaster                    |
|         | Jane Doe                |                                          |

- Only the **first row** of each group should contain the project title and group number.
- Group members follow below without repeating the group number.

---

### 🚀 How to Run the App Locally

```bash
# Clone the repo
git clone https://github.com/KrishnaAnnavaram/pick-n-play.git
cd pick-n-play

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
