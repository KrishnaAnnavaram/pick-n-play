import pandas as pd

def parse_excel(file):
    # Read the Excel file
    df = pd.read_excel(file)

    # Check for required columns
    required_cols = {"Group", "Student Name", "Project Idea"}
    if not required_cols.issubset(df.columns):
        raise ValueError("Excel must contain 'Group', 'Student Name', and 'Project Idea' columns.")

    groups = []
    current_group = None

    # Iterate row-by-row to build group structure
    for _, row in df.iterrows():
        group = row["Group"]
        student = row["Student Name"]
        project = row["Project Idea"]

        if pd.notna(group):
            # Start a new group
            if current_group:
                groups.append(current_group)
            current_group = {
                "group_number": group,
                "project_title": project if pd.notna(project) else "",
                "members": [student] if pd.notna(student) else []
            }
        else:
            # Continue with existing group
            if current_group and pd.notna(student):
                current_group["members"].append(student)

    # Append the last group
    if current_group:
        groups.append(current_group)

    return groups
