import openai

def generate_backup_summary(summary_data):
    prompt = (
        f"A backup operation was performed on folder '{summary_data['directory']}'.\n"
        f"- {summary_data['total_files']} total files\n"
        f"- {summary_data['successful_uploads']} uploaded successfully\n"
        f"- {len(summary_data['failed_integrity'])} failed integrity check: {summary_data['failed_integrity']}\n"
        "Write a short, clear notification message summarizing this backup."
    )

    openai.api_key = "your-openai-api-key"

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
