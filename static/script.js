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
        const allSuggestions = ['Florence','Milan','Naples','Edinburgh','Glasgow','Manchester','Birmingham','Liverpool',
        'Bristol','Cardiff','Belfast','Dublin','New York','Los Angeles','Chicago','San Francisco','Miami','London','Tokyo',
        'Sydney','Paris','Rome','Cairo','Rio de Janeiro','Dubai','Seattle','Toronto','Berlin','Amsterdam','Barcelona','Munich',
        'Vienna','Prague','Budapest','Athens','Istanbul','Moscow','Stockholm','Oslo','Copenhagen','Helsinki','Reykjavik',
        'Dubrovnik','Santorini','Lisbon','Madrid','Seville','Jaipur','Delhi','Agra','Bangkok','Phuket','Chiang Mai',
        'Krabi','Kyoto','Osaka','Hiroshima','Nara','Sapporo','Okinawa','Melbourne','Brisbane','Perth','Adelaide','Auckland',
        'Wellington','Christchurch','Venice','Mumbai','Seoul','Beijing','Shanghai','Hong Kong','Singapore','Kuala Lumpur',
        'Bangalore','Chennai'];
        return allSuggestions.filter(function(suggestion) {
            return suggestion.toLowerCase().startsWith(inputText);
        });
    }
});