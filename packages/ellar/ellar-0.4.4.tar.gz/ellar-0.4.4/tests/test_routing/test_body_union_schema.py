from typing import Union

from ellar.common import Body, post
from ellar.common.serializer import serialize_object
from ellar.openapi import OpenAPIDocumentBuilder
from ellar.testing import Test

from .sample import Item, OtherItem

tm = Test.create_test_module()


@post("/items/")
def save_union_body_and_embedded_body(
    item: Union[OtherItem, Item], qty: int = Body(12)
):
    return {"item": item, "qty": qty}


app = tm.create_application()
app.router.append(save_union_body_and_embedded_body)

client = tm.get_test_client()


item_openapi_schema = {
    "openapi": "3.0.2",
    "info": {"title": "Ellar API Docs", "version": "1.0.0"},
    "paths": {
        "/items/": {
            "post": {
                "operationId": "save_union_body_and_embedded_body_items__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/body_save_union_body_and_embedded_body_items__post"
                            }
                        }
                    },
                    "required": True,
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {"title": "Response Model", "type": "object"}
                            }
                        },
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        },
                    },
                },
            }
        }
    },
    "components": {
        "schemas": {
            "HTTPValidationError": {
                "title": "HTTPValidationError",
                "required": ["detail"],
                "type": "object",
                "properties": {
                    "detail": {
                        "title": "Details",
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/ValidationError"},
                    }
                },
            },
            "Item": {
                "title": "Item",
                "type": "object",
                "properties": {"name": {"title": "Name", "type": "string"}},
            },
            "OtherItem": {
                "title": "OtherItem",
                "required": ["price"],
                "type": "object",
                "properties": {"price": {"title": "Price", "type": "integer"}},
            },
            "ValidationError": {
                "title": "ValidationError",
                "required": ["loc", "msg", "type"],
                "type": "object",
                "properties": {
                    "loc": {
                        "title": "Location",
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "msg": {"title": "Message", "type": "string"},
                    "type": {"title": "Error Type", "type": "string"},
                },
            },
            "body_save_union_body_and_embedded_body_items__post": {
                "title": "body_save_union_body_and_embedded_body_items__post",
                "required": ["item"],
                "type": "object",
                "properties": {
                    "item": {
                        "title": "Item",
                        "anyOf": [
                            {"$ref": "#/components/schemas/OtherItem"},
                            {"$ref": "#/components/schemas/Item"},
                        ],
                    },
                    "qty": {"title": "Qty", "type": "integer", "default": 12},
                },
            },
        }
    },
    "tags": [],
}


def test_item_openapi_schema():
    document = serialize_object(OpenAPIDocumentBuilder().build_document(app))
    assert document == item_openapi_schema


def test_post_other_item():
    response = client.post("/items/", json={"item": {"price": 100}})
    assert response.status_code == 200, response.text
    assert response.json() == {"item": {"price": 100}, "qty": 12}


def test_post_item():
    response = client.post("/items/", json={"item": {"name": "Foo"}})
    assert response.status_code == 200, response.text
    assert response.json() == {"item": {"name": "Foo"}, "qty": 12}
