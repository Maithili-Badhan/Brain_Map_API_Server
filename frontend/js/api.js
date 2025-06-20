const API_URL = "http://127.0.0.1:5000/regions";

function display(data) {
  document.getElementById("result").innerText = JSON.stringify(data, null, 2);
}

// Get all regions
function getAllRegions() {
  fetch(API_URL + "/")
    .then(res => res.json())
    .then(display)
    .catch(err => display({ error: err.message }));
}

// Get region by ID
function getOneRegion() {
  const id = document.getElementById("regionId").value;
  fetch(`${API_URL}/${id}`)
    .then(res => res.json())
    .then(display)
    .catch(err => display({ error: err.message }));
}

// Post a new region
function postRegion() {
  const payload = {
    name: "New Region",
    description: "From frontend",
    function: "Testing POST"
  };

  fetch(API_URL + "/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })
    .then(res => res.json())
    .then(display)
    .catch(err => display({ error: err.message }));
}

// Update an existing region
function updateRegion() {
  const id = document.getElementById("regionId").value;
  const payload = {
    name: "Updated from Frontend",
    function: "Updated via UI"
  };

  fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })
    .then(res => res.json())
    .then(display)
    .catch(err => display({ error: err.message }));
}

// Delete a region
function deleteRegion() {
  const id = document.getElementById("regionId").value;
  fetch(`${API_URL}/${id}`, {
    method: "DELETE"
  })
    .then(res => res.json())
    .then(display)
    .catch(err => display({ error: err.message }));
}