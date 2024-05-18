# canvasDiscussionGrader
# dH 5/18/24
# Fresno, CA
# Access a canvas course discussion, summarize it, assign grades and remarks (reply)

import requests


def get_canvas_courses(api_key, base_url):
    headers = {'Authorization': f'Bearer {api_key}'}
    endpoint = f'{base_url}/api/v1/courses'
    courses = []

    while endpoint:
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            courses_page = response.json()
            courses.extend(courses_page)

            # Check if there's a next page
            if 'next' in response.links:
                endpoint = response.links['next']['url']
            else:
                endpoint = None
        else:
            print(f"Failed to retrieve courses: {response.status_code}, {response.text}")
            break

    for course in courses:
        print(f"Course Name: {course['name']}, Course ID: {course['id']}")


if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Canvas API key
    API_KEY = "secret API key goes here"
    # Replace 'YOUR_CANVAS_BASE_URL' with your Canvas instance URL, e.g., 'https://canvas.instructure.com'
    BASE_URL = "https://scccd.instructure.com"

    get_canvas_courses(API_KEY, BASE_URL)
