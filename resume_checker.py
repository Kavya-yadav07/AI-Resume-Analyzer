print("=== Smart Resume Analyzer ===")

resume = input("\nPaste your resume text here:\n").lower()

# Skill lists
tech_skills = ["python", "java", "sql", "html", "css", "javascript", "machine learning", "ai"]
soft_skills = ["communication", "teamwork", "leadership", "problem solving", "adaptability"]

found_tech = []
found_soft = []

# Check technical skills
for skill in tech_skills:
    if skill in resume:
        found_tech.append(skill)

# Check soft skills
for skill in soft_skills:
    if skill in resume:
        found_soft.append(skill)

# Report
print("\n--- Analysis Report ---")

if found_tech:
    print("Technical skills found:", ", ".join(found_tech))
else:
    print("No technical skills detected")

if found_soft:
    print("Soft skills found:", ", ".join(found_soft))
else:
    print("No soft skills detected")

# Score calculation
score = len(found_tech) * 2 + len(found_soft)

print(f"\nResume Score: {score}/10")

if score >= 7:
    print("Excellent profile 🚀 Ready for placements!")
elif score >= 4:
    print("Good start 🙂 Improve with more projects/tools.")
else:
    print("Needs improvement. Add skills & experience.")

# Suggestions
print("\nSuggestions:")
print("- Add project experience")
print("- Mention tools & technologies")
print("- Include measurable achievements")