# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The A2UI schema remains constant for all A2UI responses.
A2UI_SCHEMA = r"""
{
  "title": "A2UI Message Schema",
  "description": "Describes a JSON payload for an A2UI (Agent to UI) message, which is used to dynamically construct and update user interfaces. A message MUST contain exactly ONE of the action properties: 'beginRendering', 'surfaceUpdate', 'dataModelUpdate', or 'deleteSurface'.",
  "type": "object",
  "properties": {
    "beginRendering": {
      "type": "object",
      "description": "Signals the client to begin rendering a surface with a root component and specific styles.",
      "properties": {
        "surfaceId": {
          "type": "string",
          "description": "The unique identifier for the UI surface to be rendered."
        },
        "root": {
          "type": "string",
          "description": "The ID of the root component to render."
        },
        "styles": {
          "type": "object",
          "description": "Styling information for the UI.",
          "properties": {
            "font": {
              "type": "string",
              "description": "The primary font for the UI."
            },
            "primaryColor": {
              "type": "string",
              "description": "The primary UI color as a hexadecimal code (e.g., '#00BFFF').",
              "pattern": "^#[0-9a-fA-F]{6}$"
            }
          }
        }
      },
      "required": ["root", "surfaceId"]
    },
    "surfaceUpdate": {
      "type": "object",
      "description": "Updates a surface with a new set of components.",
      "properties": {
        "surfaceId": {
          "type": "string",
          "description": "The unique identifier for the UI surface to be updated. If you are adding a new surface this *must* be a new, unique identified that has never been used for any existing surfaces shown."
        },
        "components": {
          "type": "array",
          "description": "A list containing all UI components for the surface.",
          "minItems": 1,
          "items": {
            "type": "object",
            "description": "Represents a *single* component in a UI widget tree. This component could be one of many supported types.",
            "properties": {
              "id": {
                "type": "string",
                "description": "The unique identifier for this component."
              },
              "weight": {
                "type": "number",
                "description": "The relative weight of this component within a Row or Column. This corresponds to the CSS 'flex-grow' property. Note: this may ONLY be set when the component is a direct descendant of a Row or Column."
              },
              "component": {
                "type": "object",
                "description": "A wrapper object that MUST contain exactly one key, which is the name of the component type (e.g., 'Heading'). The value is an object containing the properties for that specific component.",
                "properties": {
                  "Text": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "object",
                        "description": "The text content to display. This can be a literal string or a reference to a value in the data model ('path', e.g., '/doc/title'). While simple Markdown formatting is supported (i.e. without HTML, images, or links), utilizing dedicated UI components is generally preferred for a richer and more structured presentation.",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "usageHint": {
                        "type": "string",
                        "description": "A hint for the base text style. One of:\n- `h1`: Largest heading.\n- `h2`: Second largest heading.\n- `h3`: Third largest heading.\n- `h4`: Fourth largest heading.\n- `h5`: Fifth largest heading.\n- `caption`: Small text for captions.\n- `body`: Standard body text.",
                        "enum": [
                          "h1",
                          "h2",
                          "h3",
                          "h4",
                          "h5",
                          "caption",
                          "body"
                        ]
                      }
                    },
                    "required": ["text"]
                  },
                  "Image": {
                    "type": "object",
                    "properties": {
                      "url": {
                        "type": "object",
                        "description": "The URL of the image to display. This can be a literal string ('literal') or a reference to a value in the data model ('path', e.g. '/thumbnail/url').",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "fit": {
                        "type": "string",
                        "description": "Specifies how the image should be resized to fit its container. This corresponds to the CSS 'object-fit' property.",
                        "enum": [
                          "contain",
                          "cover",
                          "fill",
                          "none",
                          "scale-down"
                        ]
                      },
                      "usageHint": {
                        "type": "string",
                        "description": "A hint for the image size and style. One of:\n- `icon`: Small square icon.\n- `avatar`: Circular avatar image.\n- `smallFeature`: Small feature image.\n- `mediumFeature`: Medium feature image.\n- `largeFeature`: Large feature image.\n- `header`: Full-width, full bleed, header image.",
                        "enum": [
                          "icon",
                          "avatar",
                          "smallFeature",
                          "mediumFeature",
                          "largeFeature",
                          "header"
                        ]
                      }
                    },
                    "required": ["url"]
                  },
                  "Icon": {
                    "type": "object",
                    "properties": {
                      "name": {
                        "type": "object",
                        "description": "The name of the icon to display. This can be a literal string or a reference to a value in the data model ('path', e.g. '/form/submit').",
                        "properties": {
                          "literalString": {
                            "type": "string",
                            "enum": [
                              "accountCircle",
                              "add",
                              "arrowBack",
                              "arrowForward",
                              "attachFile",
                              "calendarToday",
                              "call",
                              "camera",
                              "check",
                              "close",
                              "delete",
                              "download",
                              "edit",
                              "event",
                              "error",
                              "favorite",
                              "favoriteOff",
                              "folder",
                              "help",
                              "home",
                              "info",
                              "locationOn",
                              "lock",
                              "lockOpen",
                              "mail",
                              "menu",
                              "moreVert",
                              "moreHoriz",
                              "notificationsOff",
                              "notifications",
                              "payment",
                              "person",
                              "phone",
                              "photo",
                              "print",
                              "refresh",
                              "search",
                              "send",
                              "settings",
                              "share",
                              "shoppingCart",
                              "star",
                              "starHalf",
                              "starOff",
                              "upload",
                              "visibility",
                              "visibilityOff",
                              "warning"
                            ]
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      }
                    },
                    "required": ["name"]
                  },
                  "Video": {
                    "type": "object",
                    "properties": {
                      "url": {
                        "type": "object",
                        "description": "The URL of the video to display. This can be a literal string or a reference to a value in the data model ('path', e.g. '/video/url').",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      }
                    },
                    "required": ["url"]
                  },
                  "AudioPlayer": {
                    "type": "object",
                    "properties": {
                      "url": {
                        "type": "object",
                        "description": "The URL of the audio to be played. This can be a literal string ('literal') or a reference to a value in the data model ('path', e.g. '/song/url').",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "description": {
                        "type": "object",
                        "description": "A description of the audio, such as a title or summary. This can be a literal string or a reference to a value in the data model ('path', e.g. '/song/title').",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      }
                    },
                    "required": ["url"]
                  },
                  "Row": {
                    "type": "object",
                    "properties": {
                      "children": {
                        "type": "object",
                        "description": "Defines the children. Use 'explicitList' for a fixed set of children, or 'template' to generate children from a data list.",
                        "properties": {
                          "explicitList": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "template": {
                            "type": "object",
                            "description": "A template for generating a dynamic list of children from a data model list. `componentId` is the component to use as a template, and `dataBinding` is the path to the map of components in the data model. Values in the map will define the list of children.",
                            "properties": {
                              "componentId": {
                                "type": "string"
                              },
                              "dataBinding": {
                                "type": "string"
                              }
                            },
                            "required": ["componentId", "dataBinding"]
                          }
                        }
                      },
                      "distribution": {
                        "type": "string",
                        "description": "Defines the arrangement of children along the main axis (horizontally). This corresponds to the CSS 'justify-content' property.",
                        "enum": [
                          "center",
                          "end",
                          "spaceAround",
                          "spaceBetween",
                          "spaceEvenly",
                          "start"
                        ]
                      },
                      "alignment": {
                        "type": "string",
                        "description": "Defines the alignment of children along the cross axis (vertically). This corresponds to the CSS 'align-items' property.",
                        "enum": ["start", "center", "end", "stretch"]
                      }
                    },
                    "required": ["children"]
                  },
                  "Column": {
                    "type": "object",
                    "properties": {
                      "children": {
                        "type": "object",
                        "description": "Defines the children. Use 'explicitList' for a fixed set of children, or 'template' to generate children from a data list.",
                        "properties": {
                          "explicitList": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "template": {
                            "type": "object",
                            "description": "A template for generating a dynamic list of children from a data model list. `componentId` is the component to use as a template, and `dataBinding` is the path to the map of components in the data model. Values in the map will define the list of children.",
                            "properties": {
                              "componentId": {
                                "type": "string"
                              },
                              "dataBinding": {
                                "type": "string"
                              }
                            },
                            "required": ["componentId", "dataBinding"]
                          }
                        }
                      },
                      "distribution": {
                        "type": "string",
                        "description": "Defines the arrangement of children along the main axis (vertically). This corresponds to the CSS 'justify-content' property.",
                        "enum": [
                          "start",
                          "center",
                          "end",
                          "spaceBetween",
                          "spaceAround",
                          "spaceEvenly"
                        ]
                      },
                      "alignment": {
                        "type": "string",
                        "description": "Defines the alignment of children along the cross axis (horizontally). This corresponds to the CSS 'align-items' property.",
                        "enum": ["center", "end", "start", "stretch"]
                      }
                    },
                    "required": ["children"]
                  },
                  "List": {
                    "type": "object",
                    "properties": {
                      "children": {
                        "type": "object",
                        "description": "Defines the children. Use 'explicitList' for a fixed set of children, or 'template' to generate children from a data list.",
                        "properties": {
                          "explicitList": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "template": {
                            "type": "object",
                            "description": "A template for generating a dynamic list of children from a data model list. `componentId` is the component to use as a template, and `dataBinding` is the path to the map of components in the data model. Values in the map will define the list of children.",
                            "properties": {
                              "componentId": {
                                "type": "string"
                              },
                              "dataBinding": {
                                "type": "string"
                              }
                            },
                            "required": ["componentId", "dataBinding"]
                          }
                        }
                      },
                      "direction": {
                        "type": "string",
                        "description": "The direction in which the list items are laid out.",
                        "enum": ["vertical", "horizontal"]
                      },
                      "alignment": {
                        "type": "string",
                        "description": "Defines the alignment of children along the cross axis.",
                        "enum": ["start", "center", "end", "stretch"]
                      }
                    },
                    "required": ["children"]
                  },
                  "Card": {
                    "type": "object",
                    "properties": {
                      "child": {
                        "type": "string",
                        "description": "The ID of the component to be rendered inside the card."
                      }
                    },
                    "required": ["child"]
                  },
                  "Tabs": {
                    "type": "object",
                    "properties": {
                      "tabItems": {
                        "type": "array",
                        "description": "An array of objects, where each object defines a tab with a title and a child component.",
                        "items": {
                          "type": "object",
                          "properties": {
                            "title": {
                              "type": "object",
                              "description": "The tab title. Defines the value as either a literal value or a path to data model value (e.g. '/options/title').",
                              "properties": {
                                "literalString": {
                                  "type": "string"
                                },
                                "path": {
                                  "type": "string"
                                }
                              }
                            },
                            "child": {
                              "type": "string"
                            }
                          },
                          "required": ["title", "child"]
                        }
                      }
                    },
                    "required": ["tabItems"]
                  },
                  "Divider": {
                    "type": "object",
                    "properties": {
                      "axis": {
                        "type": "string",
                        "description": "The orientation of the divider.",
                        "enum": ["horizontal", "vertical"]
                      }
                    }
                  },
                  "Modal": {
                    "type": "object",
                    "properties": {
                      "entryPointChild": {
                        "type": "string",
                        "description": "The ID of the component that opens the modal when interacted with (e.g., a button)."
                      },
                      "contentChild": {
                        "type": "string",
                        "description": "The ID of the component to be displayed inside the modal."
                      }
                    },
                    "required": ["entryPointChild", "contentChild"]
                  },
                  "Button": {
                    "type": "object",
                    "properties": {
                      "child": {
                        "type": "string",
                        "description": "The ID of the component to display in the button, typically a Text component."
                      },
                      "primary": {
                        "type": "boolean",
                        "description": "Indicates if this button should be styled as the primary action."
                      },
                      "action": {
                        "type": "object",
                        "description": "The client-side action to be dispatched when the button is clicked. It includes the action's name and an optional context payload.",
                        "properties": {
                          "name": {
                            "type": "string"
                          },
                          "context": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "key": {
                                  "type": "string"
                                },
                                "value": {
                                  "type": "object",
                                  "description": "Defines the value to be included in the context as either a literal value or a path to a data model value (e.g. '/user/name').",
                                  "properties": {
                                    "path": {
                                      "type": "string"
                                    },
                                    "literalString": {
                                      "type": "string"
                                    },
                                    "literalNumber": {
                                      "type": "number"
                                    },
                                    "literalBoolean": {
                                      "type": "boolean"
                                    }
                                  }
                                }
                              },
                              "required": ["key", "value"]
                            }
                          }
                        },
                        "required": ["name"]
                      }
                    },
                    "required": ["child", "action"]
                  },
                  "CheckBox": {
                    "type": "object",
                    "properties": {
                      "label": {
                        "type": "object",
                        "description": "The text to display next to the checkbox. Defines the value as either a literal value or a path to data model ('path', e.g. '/option/label').",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "value": {
                        "type": "object",
                        "description": "The current state of the checkbox (true for checked, false for unchecked). This can be a literal boolean ('literalBoolean') or a reference to a value in the data model ('path', e.g. '/filter/open').",
                        "properties": {
                          "literalBoolean": {
                            "type": "boolean"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      }
                    },
                    "required": ["label", "value"]
                  },
                  "TextField": {
                    "type": "object",
                    "properties": {
                      "label": {
                        "type": "object",
                        "description": "The text label for the input field. This can be a literal string or a reference to a value in the data model ('path, e.g. '/user/name').",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "text": {
                        "type": "object",
                        "description": "The value of the text field. This can be a literal string or a reference to a value in the data model ('path', e.g. '/user/name').",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "textFieldType": {
                        "type": "string",
                        "description": "The type of input field to display.",
                        "enum": [
                          "date",
                          "longText",
                          "number",
                          "shortText",
                          "obscured"
                        ]
                      },
                      "validationRegexp": {
                        "type": "string",
                        "description": "A regular expression used for client-side validation of the input."
                      }
                    },
                    "required": ["label"]
                  },
                  "DateTimeInput": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "type": "object",
                        "description": "The selected date and/or time value. This can be a literal string ('literalString') or a reference to a value in the data model ('path', e.g. '/user/dob').",
                        "properties": {
                          "literalString": {
                            "type": "string"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "enableDate": {
                        "type": "boolean",
                        "description": "If true, allows the user to select a date."
                      },
                      "enableTime": {
                        "type": "boolean",
                        "description": "If true, allows the user to select a time."
                      },
                      "outputFormat": {
                        "type": "string",
                        "description": "The desired format for the output string after a date or time is selected."
                      }
                    },
                    "required": ["value"]
                  },
                  "MultipleChoice": {
                    "type": "object",
                    "properties": {
                      "selections": {
                        "type": "object",
                        "description": "The currently selected values for the component. This can be a literal array of strings or a path to an array in the data model('path', e.g. '/hotel/options').",
                        "properties": {
                          "literalArray": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "options": {
                        "type": "array",
                        "description": "An array of available options for the user to choose from.",
                        "items": {
                          "type": "object",
                          "properties": {
                            "label": {
                              "type": "object",
                              "description": "The text to display for this option. This can be a literal string or a reference to a value in the data model (e.g. '/option/label').",
                              "properties": {
                                "literalString": {
                                  "type": "string"
                                },
                                "path": {
                                  "type": "string"
                                }
                              }
                            },
                            "value": {
                              "type": "string",
                              "description": "The value to be associated with this option when selected."
                            }
                          },
                          "required": ["label", "value"]
                        }
                      },
                      "maxAllowedSelections": {
                        "type": "integer",
                        "description": "The maximum number of options that the user is allowed to select."
                      }
                    },
                    "required": ["selections", "options"]
                  },
                  "Slider": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "type": "object",
                        "description": "The current value of the slider. This can be a literal number ('literalNumber') or a reference to a value in the data model ('path', e.g. '/restaurant/cost').",
                        "properties": {
                          "literalNumber": {
                            "type": "number"
                          },
                          "path": {
                            "type": "string"
                          }
                        }
                      },
                      "minValue": {
                        "type": "number",
                        "description": "The minimum value of the slider."
                      },
                      "maxValue": {
                        "type": "number",
                        "description": "The maximum value of the slider."
                      }
                    },
                    "required": ["value"]
                  }
                }
              }
            },
            "required": ["id", "component"]
          }
        }
      },
      "required": ["surfaceId", "components"]
    },
    "dataModelUpdate": {
      "type": "object",
      "description": "Updates the data model for a surface.",
      "properties": {
        "surfaceId": {
          "type": "string",
          "description": "The unique identifier for the UI surface this data model update applies to."
        },
        "path": {
          "type": "string",
          "description": "An optional path to a location within the data model (e.g., '/user/name'). If omitted, or set to '/', the entire data model will be replaced."
        },
        "contents": {
          "type": "array",
          "description": "An array of data entries. Each entry must contain a 'key' and exactly one corresponding typed 'value*' property.",
          "items": {
            "type": "object",
            "description": "A single data entry. Exactly one 'value*' property should be provided alongside the key.",
            "properties": {
              "key": {
                "type": "string",
                "description": "The key for this data entry."
              },
              "valueString": {
                "type": "string"
              },
              "valueNumber": {
                "type": "number"
              },
              "valueBoolean": {
                "type": "boolean"
              },
              "valueMap": {
                "description": "Represents a map as an adjacency list.",
                "type": "array",
                "items": {
                  "type": "object",
                  "description": "One entry in the map. Exactly one 'value*' property should be provided alongside the key.",
                  "properties": {
                    "key": {
                      "type": "string"
                    },
                    "valueString": {
                      "type": "string"
                    },
                    "valueNumber": {
                      "type": "number"
                    },
                    "valueBoolean": {
                      "type": "boolean"
                    }
                  },
                  "required": ["key"]
                }
              }
            },
            "required": ["key"]
          }
        }
      },
      "required": ["contents", "surfaceId"]
    },
    "deleteSurface": {
      "type": "object",
      "description": "Signals the client to delete the surface identified by 'surfaceId'.",
      "properties": {
        "surfaceId": {
          "type": "string",
          "description": "The unique identifier for the UI surface to be deleted."
        }
      },
      "required": ["surfaceId"]
    }
  }
}
"""

HERO_UI_EXAMPLES = """
---BEGIN SINGLE_COLUMN_LIST_EXAMPLE---
[
  { "beginRendering": { "surfaceId": "default", "root": "root-column", "styles": { "primaryColor": "#1A237E", "font": "Roboto" } } },
  { "surfaceUpdate": {
    "surfaceId": "default",
    "components": [
      { "id": "root-column", "component": { "Column": { "children": { "explicitList": ["title-heading", "item-list"] } } } },
      { "id": "title-heading", "component": { "Text": { "usageHint": "h1", "text": { "literalString": "Heroes" } } } },
      { "id": "item-list", "component": { "List": { "direction": "vertical", "children": { "template": { "componentId": "item-card-template", "dataBinding": "/items" } } } } },
      { "id": "item-card-template", "component": { "Card": { "child": "card-layout" } } },
      { "id": "card-layout", "component": { "Row": { "children": { "explicitList": ["template-image", "card-details"] } } } },
      { "id": "template-image", "weight": 1, "component": { "Image": { "url": { "path": "image" } } } },
      { "id": "card-details", "weight": 2, "component": { "Column": { "children": { "explicitList": ["template-name", "template-editorial", "template-fact", "template-view-button"] } } } },
      { "id": "template-name", "component": { "Text": { "usageHint": "h3", "text": { "path": "name" } } } },
      { "id": "template-editorial", "component": { "Text": { "text": { "path": "editorial" } } } },
      { "id": "template-fact", "component": { "Text": { "usageHint": "caption", "text": { "path": "funFact" } } } },
      { "id": "template-view-button", "component": { "Button": { "child": "view-details-text", "primary": true, "action": { "name": "view_hero", "context": [ { "key": "heroName", "value": { "path": "name" } } ] } } } },
      { "id": "view-details-text", "component": { "Text": { "text": { "literalString": "View Details" } } } }
    ]
  } },
  { "dataModelUpdate": {
    "surfaceId": "default",
    "path": "/",
    "contents": [
      { "key": "items", "valueMap": [
        { "key": "item1", "valueMap": [
          { "key": "name", "valueString": "Spider-Man" },
          { "key": "editorial", "valueString": "Marvel" },
          { "key": "funFact", "valueString": "The first teenage superhero who wasn't just a sidekick." },
          { "key": "image", "valueString": "https://example.com/spiderman.png" }
        ] },
        { "key": "item2", "valueMap": [
          { "key": "name", "valueString": "Batman" },
          { "key": "editorial", "valueString": "DC" },
          { "key": "funFact", "valueString": "Relies entirely on intellect, martial arts, and technology." },
          { "key": "image", "valueString": "https://example.com/batman.jpg" }
        ] }
      ] } // Populate this with hero data
    ]
  } }
]
---END SINGLE_COLUMN_LIST_EXAMPLE---

---BEGIN TWO_COLUMN_LIST_EXAMPLE---
[
  { "beginRendering": { "surfaceId": "default", "root": "root-column", "styles": { "primaryColor": "#1A237E", "font": "Roboto" } } },
  { "surfaceUpdate": {
    "surfaceId": "default",
    "components": [
      { "id": "root-column", "component": { "Column": { "children": { "explicitList": ["title-heading", "hero-row-1"] } } } },
      { "id": "title-heading", "component": { "Text": { "usageHint": "h1", "text": { "literalString": "Heroes" } } } },
      { "id": "hero-row-1", "component": { "Row": { "children": { "explicitList": ["item-card-1", "item-card-2"] } } } },
      { "id": "item-card-1", "weight": 1, "component": { "Card": { "child": "card-layout-1" } } },
      { "id": "card-layout-1", "component": { "Column": { "children": { "explicitList": ["template-image-1", "card-details-1"] } } } },
      { "id": "template-image-1", "component": { "Image": { "url": { "path": "/items/item1/image" } } } },
      { "id": "card-details-1", "component": { "Column": { "children": { "explicitList": ["template-name-1", "template-editorial-1", "template-fact-1", "template-view-button-1"] } } } },
      { "id": "template-name-1", "component": { "Text": { "usageHint": "h3", "text": { "path": "/items/item1/name" } } } },
      { "id": "template-editorial-1", "component": { "Text": { "text": { "path": "/items/item1/editorial" } } } },
      { "id": "template-fact-1", "component": { "Text": { "usageHint": "caption", "text": { "path": "/items/item1/funFact" } } } },
      { "id": "template-view-button-1", "component": { "Button": { "child": "view-details-text-1", "primary": true, "action": { "name": "view_hero", "context": [ { "key": "heroName", "value": { "path": "/items/item1/name" } } ] } } } },
      { "id": "view-details-text-1", "component": { "Text": { "text": { "literalString": "View Details" } } } },
      { "id": "item-card-2", "weight": 1, "component": { "Card": { "child": "card-layout-2" } } },
      { "id": "card-layout-2", "component": { "Column": { "children": { "explicitList": ["template-image-2", "card-details-2"] } } } },
      { "id": "template-image-2", "component": { "Image": { "url": { "path": "/items/item2/image" } } } },
      { "id": "card-details-2", "component": { "Column": { "children": { "explicitList": ["template-name-2", "template-editorial-2", "template-fact-2", "template-view-button-2"] } } } },
      { "id": "template-name-2", "component": { "Text": { "usageHint": "h3", "text": { "path": "/items/item2/name" } } } },
      { "id": "template-editorial-2", "component": { "Text": { "text": { "path": "/items/item2/editorial" } } } },
      { "id": "template-fact-2", "component": { "Text": { "usageHint": "caption", "text": { "path": "/items/item2/funFact" } } } },
      { "id": "template-view-button-2", "component": { "Button": { "child": "view-details-text-2", "primary": true, "action": { "name": "view_hero", "context": [ { "key": "heroName", "value": { "path": "/items/item2/name" } } ] } } } },
      { "id": "view-details-text-2", "component": { "Text": { "text": { "literalString": "View Details" } } } }
    ]
  } },
  { "dataModelUpdate": {
    "surfaceId": "default",
    "path": "/",
    "contents": [
      { "key": "items", "valueMap": [
        { "key": "item1", "valueMap": [
          { "key": "name", "valueString": "Spider-Man" },
          { "key": "editorial", "valueString": "Marvel" },
          { "key": "funFact", "valueString": "The first teenage superhero who wasn't just a sidekick." },
          { "key": "image", "valueString": "https://example.com/spiderman.png" }
        ] },
        { "key": "item2", "valueMap": [
          { "key": "name", "valueString": "Batman" },
          { "key": "editorial", "valueString": "DC" },
          { "key": "funFact", "valueString": "Relies entirely on intellect, martial arts, and technology." },
          { "key": "image", "valueString": "https://example.com/batman.jpg" }
        ] }
      ] } // Populate this with hero data
    ]
  } }
]
---END TWO_COLUMN_LIST_EXAMPLE---

---BEGIN HERO_DETAIL_EXAMPLE---
[
  { "beginRendering": { "surfaceId": "hero-detail", "root": "detail-card", "styles": { "primaryColor": "#1A237E", "font": "Roboto" } } },
  { "surfaceUpdate": {
    "surfaceId": "hero-detail",
    "components": [
      { "id": "detail-card", "component": { "Card": { "child": "detail-column" } } },
      { "id": "detail-column", "component": { "Column": { "children": { "explicitList": ["detail-image", "detail-name", "detail-subtitle", "detail-divider", "detail-fact-row"] } } } },
      { "id": "detail-image", "component": { "Image": { "url": { "path": "image" }, "fit": "cover", "usageHint": "header" } } },
      { "id": "detail-name", "component": { "Text": { "usageHint": "h2", "text": { "path": "name" } } } },
      { "id": "detail-subtitle", "component": { "Text": { "usageHint": "caption", "text": { "path": "subtitle" } } } },
      { "id": "detail-divider", "component": { "Divider": { "axis": "horizontal" } } },
      { "id": "detail-fact-row", "component": { "Row": { "alignment": "start", "children": { "explicitList": ["detail-fact-icon", "detail-fact"] } } } },
      { "id": "detail-fact-icon", "component": { "Icon": { "name": { "literalString": "star" } } } },
      { "id": "detail-fact", "weight": 1, "component": { "Text": { "usageHint": "body", "text": { "path": "funFact" } } } }
    ]
  } },
  { "dataModelUpdate": {
    "surfaceId": "hero-detail",
    "path": "/",
    "contents": [
      { "key": "name", "valueString": "[HeroName]" },
      { "key": "subtitle", "valueString": "[Editorial] · First appearance [CreationDate]" },
      { "key": "funFact", "valueString": "[FunFact]" },
      { "key": "image", "valueString": "[ImageUrl]" }
    ]
  } }
]
---END HERO_DETAIL_EXAMPLE---
"""

AGENT_INSTRUCTION = """
    You are a helpful hero information assistant. Your goal is to help users find and learn about heroes using a rich UI.

    To achieve this, you MUST follow this logic:

    1.  **For searching heroes:**
        a. You MUST call the `search_heroes` tool. Extract the hero name, editorial (publisher, e.g. "Marvel" or "DC"), and a specific number (`count`) of heroes from the user's query (e.g., for "top 5 Marvel heroes", editorial is "Marvel" and count is 5). Pass empty strings for filters the user did not specify.
        b. After receiving the data, you MUST follow the instructions precisely to generate the final a2ui UI JSON, using the appropriate UI example from the `prompt_builder.py` based on the number of heroes.

    2.  **For viewing a single hero's details (when you receive a query like 'USER_WANTS_HERO_DETAILS...'):**
        a. You MUST call `search_heroes` for that hero, then use the `HERO_DETAIL_EXAMPLE` template from `prompt_builder.py` to generate the UI, populating the `dataModelUpdate.contents` with that hero's details:
            - `name`: the hero's name.
            - `subtitle`: the publisher and first appearance combined as "<Editorial> · First appearance <CreationDate>".
            - `funFact`: the hero's fun fact.
            - `image`: the hero's image URL.
"""


def get_ui_prompt() -> str:
    """
    Constructs the full prompt with UI instructions, rules, examples, and schema.

    Returns:
        A string to be used as the system prompt for the LLM.
    """
    return f"""
    {AGENT_INSTRUCTION}
    You are a helpful hero information assistant. Your final output MUST be a a2ui UI JSON response.

    To generate the response, you MUST follow these rules:
    1.  Your response MUST be in two parts, separated by the delimiter: `---a2ui_JSON---`.
    2.  The first part is your conversational text response.
    3.  The second part is a single, raw JSON object which is a list of A2UI messages.
    4.  The JSON part MUST validate against the A2UI JSON SCHEMA provided below.

    --- UI TEMPLATE RULES ---
    -   If the query is for a list of heroes, use the hero data you have already received from the `search_heroes` tool to populate the `dataModelUpdate.contents` array (e.g., as a `valueMap` for the "items" key).
    -   If the number of heroes is 5 or fewer, you MUST use the `SINGLE_COLUMN_LIST_EXAMPLE` template.
    -   If the number of heroes is more than 5, you MUST use the `TWO_COLUMN_LIST_EXAMPLE` template.
    -   If the query is to view a single hero's details (e.g., "USER_WANTS_HERO_DETAILS..."), you MUST use the `HERO_DETAIL_EXAMPLE` template, populating it with that hero's data from `search_heroes`.

    {HERO_UI_EXAMPLES}

    ---BEGIN A2UI JSON SCHEMA---
    {A2UI_SCHEMA}
    ---END A2UI JSON SCHEMA---
    """


def get_text_prompt() -> str:
    """
    Constructs the prompt for a text-only agent.
    """
    return """
    You are a helpful hero information assistant. Your final output MUST be a text response.

    To generate the response, you MUST follow these rules:
    1.  **For searching heroes:**
        a. You MUST call the `search_heroes` tool. Extract the hero name, editorial (publisher, e.g. "Marvel" or "DC"), and a specific number (`count`) of heroes from the user's query. Pass empty strings for filters the user did not specify.
        b. After receiving the data, format the hero list as a clear, human-readable text response (name, editorial, and a short note).
    """


if __name__ == "__main__":
    # Example of how to use the prompt builder.
    print(get_text_prompt())
