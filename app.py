import streamlit as st
import requests

# Base URL for the Django REST API
BASE_URL = "http://127.0.0.1:8000/api"

# Streamlit UI
st.title("Django REST API Tester")

# Select the entity type
entity_type = st.sidebar.selectbox("Select Entity", ["Categories", "Products"])

# Function to display all entities
def display_all_entities(entity):
    response = requests.get(f"{BASE_URL}/{entity.lower()}/")
    if response.status_code == 200:
        data = response.json()
        st.write(data)
    else:
        st.error("Failed to fetch data")

# Function to create a new entity
def create_entity(entity):
    name = st.text_input("Name", key="name")
    if entity == "Product":
        description = st.text_area("Description")
        price = st.number_input("Price", min_value=0.0, step=0.01)
        category_id = st.number_input("Category ID", min_value=1, step=1)

    if st.button("Create"):
        data = {"name": name}
        if entity == "Product":
            data.update({
                "description": description,
                "price": price,
                "category": category_id
            })
        response = requests.post(f"{BASE_URL}/{entity.lower()}/", json=data)
        if response.status_code == 201:
            st.success(f"{entity} created successfully!")
        else:
            st.error("Failed to create entity")

# Function to update an entity
def update_entity(entity):
    entity_id = st.number_input(f"{entity} ID", min_value=1, step=1)
    name = st.text_input("New Name", key="update_name")
    if entity == "Product":
        description = st.text_area("New Description")
        price = st.number_input("New Price", min_value=0.0, step=0.01)
        category_id = st.number_input("New Category ID", min_value=1, step=1)

    if st.button("Update"):
        data = {"name": name}
        if entity == "Product":
            data.update({
                "description": description,
                "price": price,
                "category": category_id
            })
        response = requests.put(f"{BASE_URL}/{entity.lower()}/{entity_id}/", json=data)
        if response.status_code == 200:
            st.success(f"{entity} updated successfully!")
        else:
            st.error("Failed to update entity")

# Function to delete an entity
def delete_entity(entity):
    entity_id = st.number_input(f"{entity} ID to Delete", min_value=1, step=1)
    if st.button("Delete"):
        response = requests.delete(f"{BASE_URL}/{entity.lower()}/{entity_id}/")
        if response.status_code == 204:
            st.success(f"{entity} deleted successfully!")
        else:
            st.error("Failed to delete entity")

# Function to search/filter entities
def search_entities(entity):
    search_term = st.text_input("Search Term (Name)")
    created_at = st.text_input("Filter by Date (YYYY-MM-DD)")

    params = {}
    if search_term:
        params["search"] = search_term
    if created_at:
        params["created_at"] = created_at

    if st.button("Search"):
        response = requests.get(f"{BASE_URL}/{entity.lower()}/", params=params)
        if response.status_code == 200:
            data = response.json()
            st.write(data)
        else:
            st.error("Failed to search entities")

# Display entity options
st.sidebar.subheader(f"{entity_type} Actions")
action = st.sidebar.selectbox("Select Action", ["View All", "Create", "Update", "Delete", "Search/Filter"])

if action == "View All":
    display_all_entities(entity_type)
elif action == "Create":
    create_entity(entity_type)
elif action == "Update":
    update_entity(entity_type)
elif action == "Delete":
    delete_entity(entity_type)
elif action == "Search/Filter":
    search_entities(entity_type)
