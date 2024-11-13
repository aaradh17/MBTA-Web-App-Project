# MBTA-Web-App-Project

This is the base repository for Web App project. Please read the [instructions](instructions.md) for details.

# MBTA Station Finder Project

## Team Members
Aaradh Benara & Felipe McCoy

### Project Overview

This project involved developing a web application to help users find the nearest MBTA (Massachusetts Bay Transportation Authority) station based on a user-provided address or place name. The web app integrates two main APIs: **Mapbox** for geocoding (to get latitude and longitude of the place) and **MBTA** for finding the nearest station and its wheelchair accessibility. The application is developed using Python, Flask, and HTML/CSS for frontend styling.

#### Main Objectives
- Integrate web APIs (Mapbox and MBTA).
- Retrieve and process structured data (JSON).
- Develop a simple but functional web app using Flask.
- Design an interactive UI with form handling and result display.

---

## Reflection

### Development Process and Challenges

In this project, we faced multiple challenges around API integration, handling structured JSON data, and building a responsive web interface.
1. **API Integration**: Understanding and implementing API calls for Mapbox and MBTA was a crucial first step. Familiarity with URL encoding, error handling, and JSON parsing was essential, as well as ensuring API keys remained secure.
2. **Testing and Debugging**: Testing the API calls with various addresses helped identify edge cases (e.g., addresses with no nearby MBTA stops). Handling SSL certificate issues and ensuring the JSON data was parsed correctly were also necessary for smooth functionality.

#### What Went Well
- The integration between the Mapbox and MBTA APIs worked well after testing, allowing us to accurately return results for most addresses.
- Flask was effective in handling user input, form submission, and routing, making the backend straightforward to develop.

#### Challenges and Areas for Improvement
- Building a reliable error-handling mechanism for cases where no nearby MBTA station was available could improve the user experience.
- More styling or even making the UI more visually appealing and dynamic.

---

### Team Collaboration

#### Work Division
- Felipe focused on backend API integration and Flask routes, while Aaradh handled the HTML, and UI testing.
- Both collaborated on testing and debugging, sharing insights to streamline error handling and ensure consistent functionality.

#### Collaboration Challenges
- Aligning on coding conventions and troubleshooting remotely presented some challenges, but regular communication helped address issues effectively.
- Coordinating GitHub branches and merging changes required attention to avoid conflicts, especially with HTML modifications.

---

### Learning and AI Tool Usage

Through this project, we learned:
1. **API and JSON Handling**: This project gave hands-on experience with building dynamic URL requests and parsing JSON data, which is crucial for web applications relying on external data sources.
2. **Web Development with Flask**: Working with Flask simplified server-side handling of user input and helped reinforce concepts around routes, HTTP methods, and rendering templates.

#### AI Tool Usage
AI tools provided useful insights, especially during debugging and exploring additional features like error handling or styling tips. For instance:
- **AI Suggestions**: The AI offered code suggestions for complex tasks (like SSL context setup) and helped find efficient ways to parse JSON data.
- **Troubleshooting Support**: When encountering specific errors, AI tools assisted in pinpointing common solutions, improving efficiency in solving issues.
  
**What We Would Do Differently**: 
Looking back, starting with a clear division of tasks and implementing more testing earlier in the development cycle could have streamlined the process and reduced debugging time. Also, exploring further customization in the user interface would enhance user interaction with the application.

