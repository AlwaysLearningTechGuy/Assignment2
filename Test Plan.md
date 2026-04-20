# Test Plan: The Wonderful and Mysterious Web Application

## 1. Scope & Area Under Test (AUT)
This plan covers the validation of the Wonderful and Mysterious Web Application container.
* **APIs:** `/api/weather`, `/api/timezone`, `/api/insight`, `/api/fortune`, `/api/submit`, `/api/favorites`.
* **Workflows:** * **Data Consumption:** Fetching utility data.
    * **Data Submission:** Sending and echoing JSON payloads.
    * **Stateful Persistence:** Saving a "Favorite" and ensuring it exists in the retrieved list.

## 2. Test Execution Procedure (The "How-To")

### A. Setup Steps
1.  **Environment Isolation:** Ensure no other services are running on port `8000`.
2.  **Container Build:** Execute `docker build -t mysterious-app .` to create the latest image.
3.  **Service Launch:** Run `docker run -d -p 8000:8000 --name test-instance mysterious-app`.
4.  **Tooling Readiness:** Ensure `pytest` and `httpx` are installed within the container.

### B. Execution Steps
1.  **Connectivity Smoke Test:** Perform a `GET` request to `/docs` to ensure the OpenAPI UI is active.
2.  **Automated Suite Run:** Execute `pytest app/test_main.py` to run TC-01 through TC-09.
3.  **Manual Verification (Edge Cases):** * Use the Swagger UI (`localhost:8000/docs`) to manually submit a specific ID to `/api/favorites`.
    * Immediately call `GET /api/favorites` to verify the ID appears in the list.
4.  **Boundary Stress:** Use a script or `curl` to send a payload exceeding 1MB to verify the `413` response.

### C. What to Validate (Success Criteria)
* **Status Codes:** Verify `200/201` for success and `400/413/429` for expected failures.
* **JSON Schema:** Ensure the "Insight" object contains the `id` and `msg` keys.
* **Data Integrity:** The `received` object in the `/api/submit` response must be a bitwise match to the input.
* **Persistence:** The `favorites` array must grow in length following a successful `POST` to that endpoint (I am going to try to have real "simple" backend - though I know you do not require it).

## 3. Test Cases (Tied to Strategy)
| ID | Scenario | Priority | Method |
| :--- | :--- | :--- | :--- |
| **TC-01** | Connectivity | High | GET /api/fortune |
| **TC-02** | Echo Validation | High | POST /api/submit |
| **TC-03** | Schema Accuracy | Medium | GET /api/insight |
| **TC-06** | Rate Limiting | Medium | GET /api/fortune (Burst) |
| **TC-08** | Save Persistence| High | POST /api/favorites |

## 4. Suspension & Resumption Criteria
* **Suspend:** If the Docker container fails to stay in a "Running" state or if `404 Not Found` occurs on all endpoints.
* **Resume:** Once the `main.py` routing or `Dockerfile` configuration is corrected and the container restarts successfully.

## 5. Definition of Done (DoD)
* All 9 test cases in the Expanded Suite have been executed.
* All identified bugs (e.g., schema mismatches) are logged in the **Test Report**.
* The application passes the Performance Latency check (< 200ms).
