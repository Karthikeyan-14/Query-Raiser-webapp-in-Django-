// Sample data for demonstration (replace with actual data handling logic)
/*var previousQueries = [
    { id: 1, title: "Query 1", type: "HR" },
    { id: 2, title: "Query 2", type: "Director" },
    { id: 3, title: "Query 3", type: "HR" }
  ];
  
  // Function to populate the table with previous queries
  function populateQueryTable() {
    var queryTableBody = document.getElementById('queryTableBody');
  
    // Clear existing rows
    queryTableBody.innerHTML = '';
  
    // Populate table rows with previous queries
    previousQueries.forEach(function(query) {
      var row = document.createElement('tr');
  
      var idCell = document.createElement('td');
      idCell.textContent = query.id;
      row.appendChild(idCell);
  
      var titleCell = document.createElement('td');
      titleCell.textContent = query.title;
      row.appendChild(titleCell);
  
      var typeCell = document.createElement('td');
      typeCell.textContent = query.type;
      row.appendChild(typeCell);
  
      var actionCell = document.createElement('td');
      var viewButton = document.createElement('button');
      viewButton.textContent = "View";
      viewButton.addEventListener('click', function() {
        // Replace with logic to view query details
        alert("Viewing query with ID: " + query.id);
      });
      actionCell.appendChild(viewButton);
      row.appendChild(actionCell);
  
      queryTableBody.appendChild(row);
    });
  }
  
  // Populate the table initially
  populateQueryTable();*/
  
  // Event listener for query form submission
  document.getElementById('queryForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var type = document.getElementById('type').value;
    var priority = document.getElementById('priority').value;
    var query = document.getElementById('query').value;
  
    // Here you can handle the submission of the query, like sending it to a server or storing it locally
    console.log("Type:", type);
    console.log("Priority:", priority);
    console.log("Query:", query);
  
    // Optionally, you can reset the form after submission
    // document.getElementById('queryForm').reset();
  
    // For demonstration, add the submitted query to the table
   /* var newQuery = { id: previousQueries.length + 1, title: "New Query", type: type };
    previousQueries.push(newQuery);
    populateQueryTable();*/
  });
  