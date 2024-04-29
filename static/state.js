document.addEventListener('DOMContentLoaded', function() {
    const locationInput = document.getElementById('input_state');
    const suggestionsDiv = document.getElementById('suggestions');

    locationInput.addEventListener('input', function() {
        const inputText = this.value.toLowerCase();
        const suggestions = getFilteredSuggestions(inputText);

        // Clear previous suggestions
        suggestionsDiv.innerHTML = '';

        // Add new suggestions
        suggestions.forEach(function(suggestion) {
            const option = document.createElement('div');
            option.textContent = suggestion;
            option.addEventListener('click', function() {
                locationInput.value = this.textContent;
                suggestionsDiv.innerHTML = '';
            });
            suggestionsDiv.appendChild(option);
        });
    });

    function getFilteredSuggestions(inputText) {
        // Example: Fetch suggestions from a server based on inputText
        const allSuggestions = ["ANDHRA PRADESH", "ARUNACHAL PRADESH", "ASSAM", "BIHAR", "CHHATTISGARH", "GOA", "GUJARAT", 
        "HARYANA", "HIMACHAL PRADESH", "JAMMU & KASHMIR", "JHARKHAND", "KARNATAKA", "KERALA", "MADHYA PRADESH", 
        "MAHARASHTRA", "MANIPUR", "MEGHALAYA", "MIZORAM", "NAGALAND", "ODISHA", "PUNJAB", "RAJASTHAN", "SIKKIM", 
        "TAMIL NADU", "TRIPURA", "UTTAR PRADESH", "UTTARAKHAND", "WEST BENGAL", "A & N ISLANDS", "CHANDIGARH", 
        "D & N HAVELI", "DAMAN & DIU", "DELHI UT", "LAKSHADWEEP", "PUDUCHERRY"];
        return allSuggestions.filter(function(suggestion) {
            return suggestion.toLowerCase().startsWith(inputText);
        });
    }
});