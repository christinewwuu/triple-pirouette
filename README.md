# triple-pirouette
**FridgeBuddy**

FridgeBuddy is a web application designed to help users track their groceries, reduce food waste, and plan meals effectively. It allows users to scan their grocery haul, extract a list of items, and organize them in a virtual fridge with automated expiry tracking.

**Features**

🥦 **Grocery List Extraction:** Uses AI image-to-text technology to extract grocery items from a photo and convert them into a list. Allows users to add items to their fridge.\
🧊 **Virtual Fridge:** Stores grocery items and categorizes them based on their expiry dates.\
📆 **Expiry Date Tracking:** Pulls expiry information from StillTasty to estimate shelf life.\
💡 **Waste Reduction Tips:** Provides evidence-backed advice on minimizing food waste.\
📝 **Meal Planning:** Helps users plan meals using the items available in their fridge.\

**Integrating Gumloop for Grocery Extraction**

The AI tool exports the grocery list as a URL-based TXT file.
The backend retrieves the file using the provided URL and processes the content.
Items are parsed and mapped to a structured list before being added to the virtual fridge in the database.
