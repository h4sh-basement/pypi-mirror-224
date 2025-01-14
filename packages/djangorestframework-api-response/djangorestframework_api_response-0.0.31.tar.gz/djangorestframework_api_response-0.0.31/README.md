# Django Rest Framework API Response

The `djangorestframework-api-response` is a utility package designed to streamline and standardize the API response formats for projects using the Django Rest Framework (DRF). With an emphasis on clarity and simplicity, this package provides predefined views and methods that allow developers to send structured success and error responses consistently. Furthermore, it introduces enhanced pagination capabilities, ensuring that results are not only paginated but also paired with relevant metadata.

## Key Features:
1. **Standardized Response Formats:** Ensure that all your API endpoints adhere to a uniform response structure, making it easier for frontend developers and other consumers of your API to predict and handle responses.

2. **Error Handling:** Simplify the process of sending error messages with the right HTTP status codes, improving API clarity and consumer feedback.

3. **Enhanced Pagination:** Go beyond basic pagination by providing additional metadata with paginated results, offering a clearer and richer data presentation for consumers of your API.

4. **Ease of Use:** With intuitive base views and helper methods, integrating the package into your existing DRF project is straightforward.

By adopting the `djangorestframework-api-response`, developers can reduce boilerplate, enhance consistency, and ensure that their DRF projects are more maintainable and consumer-friendly.

## Getting Started
To use the DjangoRestFramework API Response package, follow these steps:

1. Install the package
Install the package in your Django Rest Framework project by running the following command:
```bash
pip install djangorestframework-api-response
```

2. Add to Django installed apps
Add *'rest_framework_api'* to your Django installed apps
```python
INSTALLED_APPS = [
    ...
    'rest_framework_api',
]
```

3. Import the StandardAPIView class
In your Django views, import the StandardAPIView class from the package:
```python
from rest_framework_api.views import StandardAPIView
```

## How to Use

When building API views with Django Rest Framework, leverage the `StandardAPIView` as your base view class. This simplifies response management and ensures consistent structures across endpoints. Here are the methods provided by the `StandardAPIView`:

### Helper Functions

`send_response(data=None, status=status.HTTP_200_OK)`
* **Purpose:** Send a successful response to the client.
* **Parameters:**
    * `data`: (Optional) Data you wish to include in the response.
    * `status`: (Optional) HTTP status code for the response. Defaults to 200 OK.
* **Usage:**
```python
return self.send_response(data={"key": "value"}, status=status.HTTP_200_OK)
```

`send_error(error, status=status.HTTP_400_BAD_REQUEST)`
* **Purpose:** Send an error message response to the client.
* **Parameters:**
    * `error`: Description of the error. This is mandatory.
    * `status`: (Optional) HTTP status code for the error response. Defaults to 400 BAD 
* **Usage:**
```python
return self.send_error(error="Description of the error", status=status.HTTP_400_BAD_REQUEST)
```

`paginate_response(request, data)`
**Purpose:** Send a paginated response without extra data.
* **Parameters:**
    * `request`: The incoming request object.
    * `data`: A list or queryset of data that you wish to paginate.
* **Usage:**
```python
data = MyModel.objects.all()
return self.paginate_response(request, data)
```

`paginate_response_with_extra(request, data, extra_data)`
**Purpose:** Send a paginated response, supplemented with additional data.
* **Parameters:**
    * `request`: The incoming request object.
    * `data`: A list or queryset of data that you wish to paginate.
    * `extra_data`: Additional data that you want to send along with the paginated response.
* **Usage:**
```python
data = MyModel.objects.all()
metadata = {"summary": "This is additional summary data."}
return self.paginate_response_with_extra(request, data, extra_data=metadata)
```

### Implementation Tips:
1. When creating new API views, subclass StandardAPIView and then use the above helper methods to send your responses.

2. By following this structure, you ensure consistent response formats across your API, making it more predictable and easier for frontend developers and API consumers to handle.


### Demo Views

#### Demo Views for BaseAPIView
Let's demonstrate the sending of regular responses and errors.
```python
class BaseDemoSuccessView(BaseAPIView):
    """
    A demo view to showcase sending a successful response with BaseAPIView.
    """
    def get(self, request):
        sample_data = {
            "message": "This is a success message from BaseDemoSuccessView."
        }
        return self.send_response(data=sample_data, status_code=status.HTTP_200_OK)


class BaseDemoErrorView(BaseAPIView):
    """
    A demo view to showcase sending an error response with BaseAPIView.
    """
    def get(self, request):
        error_msg = "This is an error message from BaseDemoErrorView."
        return self.send_error(error=error_msg, status_code=status.HTTP_400_BAD_REQUEST)
```

#### Demo Views for StandardAPIView
For the StandardAPIView, the primary use cases are paginating results and paginating results with extra data.

```python
class StandardDemoPaginatedView(StandardAPIView):
    """
    A demo view to showcase basic paginated responses using StandardAPIView.
    """
    def get(self, request):
        sample_data = [
            {"id": i, "content": f"Item {i}"} for i in range(1, 51)  # 50 items
        ]
        return self.paginate_response(request, sample_data)


class StandardDemoPaginatedWithExtraView(StandardAPIView):
    """
    A demo view to showcase paginated responses with extra data using StandardAPIView.
    """
    def get(self, request):
        sample_data = [
            {"id": i, "content": f"Item {i}"} for i in range(1, 51)  # 50 items
        ]
        extra_data = {
            "metadata": "This is some extra data that accompanies the paginated results."
        }
        return self.paginate_response_with_extra(request, sample_data, extra_data=extra_data)
```

### Usage
To test these views:

1. Include them in your project's urls.py.

2. Use an API client, like Postman, or your browser to send GET requests to these views' endpoints.

**To make a request**, you can send a GET request to the URL for the view.

For example, if the view is mounted at /api/hello_world, you can send a request like this
```bash
GET /api/hello_world
```

To specify the page size and maximum page size in the request, you can use the page_size_query_param and page_size query parameters, respectively.

For example, to set the page size to 10 and the maximum page size to 100, you can include the following query parameters in the URL:
```bash
GET /api/hello_world?p=1&page_size=10&max_page_size=100
```

You can also specify the page number in the request using the **page_query_param** query parameter.

For example, to request the second page of results, you can include the following query parameter in the URL:
```bash
GET /api/hello_world?p=2
```

This will return the second page of results, based on the page size specified in the request.

3. Observe the responses to understand and verify the behavior of the BaseAPIView and StandardAPIView classes in different scenarios.

When the client sends a request with the success parameter set to true, this view will send a successful response with the message "Hello World!". Otherwise, it will send an error response with the message "Hello Errors!".

#### Normal Response

The response sent to the client will have the following format:
```json
{
    "success": true,
    "status": "200"
    "data": {
        "message": "Hello World!"
    },
}
```
or
```json
{
    "success": false,
    "status": "400",
    "error": "This is a custom error message. I am a String."
}
```

You can then use the success and data fields in the client to determine the outcome of the request and process the response accordingly.


#### Paginated Response
The response will be a paginated list of data, with the pagination metadata included in the response. The pagination metadata will include the current page number, the number of results per page, the total number of results, and the total number of pages. 

For example, if there are 10 courses in total and the page size is 3, the response will include metadata indicating that there are a total of 4 pages, with the first page containing the first 3 courses and the second page containing the next 3 courses, and so on. The data for each course will be included in the 'results' field of the response.

Here is an example of what a response might look like:
```json
{
    "success": true,
    "status": 200,
    "count": 10,
    "next": "http://example.com/api/courses?page=2",
    "previous": null,
    "data": [
    {
        "id": 1,
        "name": "Introduction to Python",
        "description": "Learn the basics of Python programming"
    },
    {
        "id": 2,
        "name": "Advanced Python Techniques",
        "description": "Learn advanced techniques for Python programming"
    },
    {
        "id": 3,
        "name": "Data Science with Python",
        "description": "Learn how to use Python for data analysis and visualization"
    }
    ]
}
```

### Django Models

**Example Views**

```python
class HelloWorldObjectPaginatedView(StandardAPIView):
    def get(self, request, format=None):
        courses = Courses.objects.all()
        if courses:
            return self.paginate_response(request, courses)
        else:
            return self.send_error('No data found')
```

This **HelloWorldObjectPaginatedView** view should work as intended, as long as the necessary dependencies are imported and the **Courses** model is correctly defined.

The view subclass **StandardAPIView** and overrides the **get** method to return a paginated list of all **courses** in the database. If the queryset courses is empty, the view will return an error response using the **send_error** method.

You can also include query parameters in the request URL to control the pagination of the response. For example, you can use the page and page_size query parameters to specify the **`page`** number and **`page size`**, respectively.
```bash
http://example.com/api/courses?p=2&page_size=10&max_page_size=100
```

This request will retrieve the second page of courses, with a page size of 10 courses per page. The response will include a paginated list of courses, along with metadata about the pagination (such as the total number of courses and URLs for the next and previous pages, if applicable).


## Overall Conclusion

The **StandardAPIView** class and the **paginate_response** method that you have implemented provide a solid foundation for creating views that return paginated responses in your API.

The **StandardAPIView** class includes several useful methods, including **send_response** and **send_error**, which allow you to easily send success and error responses from your views. The **paginate_response** method provides a convenient way to paginate data and return a paginated response to the client.

To create views using the **StandardAPIView** class, you can subclass **StandardAPIView** and override the appropriate HTTP method handler (e.g., **get**, **post**, **put**, etc.). Inside the handler method, you can call the **paginate_response** method to paginate and return the data to the client.

With this setup, you can easily create views that return paginated responses to the client using the **StandardAPIView** class and the **paginate__response** handler function.