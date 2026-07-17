
def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept" : "application/json",
            "Authorization" : "Bearer your_token_here",
            "x-api-key" : "reqres_5a2b03ef58de41cf8fb727bc125f3c38"
        }   
    )
    response = request.get("https://reqres.in/api/users?page=2")
    
    assert response.status == 200 
    
    json_data = response.json()
    print(f"\n\n{json_data}")
    
    assert json_data["data"][3]["first_name"] == "Byron"
    assert json_data["data"][5]["last_name"] == "Howell"
    
    request.dispose()
    print(f"\nTest Completed Successfully")