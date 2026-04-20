# Test Strategy: The Wonderful and Mysterious Web Application

## 1. Area Under Test (AUT)
The scope of testing covers the Wonderful and Mysterious Web Application, a FastAPI-based microservice. 
* **Wonderful Components:** Logical utility endpoints including weather data, timezone calculations, and interesting Insights.
* **Mysterious Components:** Randomized fortune generation and the stateful persistence layer (Favorites).
* **Infrastructure:** The Docker container environment and the RESTful communication interface.

## 2. General Processes & Tooling
To ensure consistency and speed, the following processes are implemented:
* **Automation-First Approach:** All functional and schema tests are automated using **Pytest** to allow for rapid regression testing.
* **Mocking:** We utilize the FastAPI **TestClient** to simulate hardware and network interaction without requiring a live deployment.
* **Containerized Execution:** Tests are executed within the Docker environment to ensure that "it works on my machine" translates to "it works in production."
* **Tools:** * **Pytest:** Core testing framework.
    * **Pydantic:** Used for automated data validation and sanitization.
    * **Docker:** For environment isolation.

## 3. Quality Metrics (Measuring Success)
We measure the "Quality" of this release based on the following metrics:
* **Test Pass Rate:** 100% success required for all "Critical" paths (Connectivity and Persistence).
* **Response Latency:** A performance metric ensuring 95% of requests are handled in under **200ms**.
* **Code Coverage:** Ensuring all major API routes are hit by at least one automated unit test.

## 4. Test Environment & Data
* **Environment:** Isolated Docker container.
* **Data Strategy:** Use of "Mock Data" for weather and fortunes to ensure test results are predictable and not dependent on external 3rd party APIs.

## 5. Risk & Issue Management
* **Risk:** In-memory storage is volatile. 
* **Mitigation:** Automated tests will verify the state exists within the lifecycle of the test runner.
