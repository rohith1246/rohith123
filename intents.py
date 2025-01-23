intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": [
                "Hi",
                "Hey",
                "Hello",
                "Good day",
                "Greetings",
                "What's up",
                "How are you",
                "Is anyone there?",
                "Hello Nextopson",
                "Hi there"
            ],
            "responses": [
                "Hello! Welcome to Nextopson. How can I assist you with your property needs?",
                "Hi there! Looking to buy, sell, or rent a property?",
                "Welcome to Nextopson! How may I help you today?",
                "Hello! I'm here to help you with all your real estate needs."
            ],
            "context_set": ""
        },
        {
            "tag": "goodbye",
            "patterns": [
                "Bye",
                "See you later",
                "Goodbye",
                "Thanks, bye",
                "See you around",
                "Catch you later",
                "Need to go",
                "Have a good day"
            ],
            "responses": [
                "Thank you for choosing Nextopson! Have a great day!",
                "Goodbye! Feel free to return if you need more assistance.",
                "See you later! Don't hesitate to reach out for any property-related help.",
                "Goodbye! Remember, we're here 24/7 for your real estate needs."
            ],
            "context_set": ""
        },
        {
            "tag": "property_search",
            "patterns": [
                "I want to buy a property",
                "Show me available properties",
                "Looking for a house",
                "Search properties",
                "Available homes",
                "Find apartment",
                "Property listings",
                "Show me houses"
            ],
            "responses": [
                "I can help you find the perfect property. Could you specify your preferred location and budget?",
                "What type of property are you looking for? We have apartments, houses, and commercial spaces available.",
                "Sure! To help you better, please tell me your preferred location, property type, and budget range.",
                "I'll help you find your ideal property. What are your requirements in terms of location and type?"
            ],
            "context_set": "property_search"
        },
        {
            "tag": "property_listing",
            "patterns": [
                "I want to sell my property",
                "How to list property",
                "List my house",
                "Sell apartment",
                "Post property",
                "How to sell",
                "Property listing process"
            ],
            "responses": [
                "Listing your property on Nextopson is easy! Just follow these steps:\n1. Create an account\n2. Click 'List Property'\n3. Fill in property details\n4. Upload photos\n5. Submit for verification",
                "Would you like to list your property? I can guide you through our zero-brokerage listing process.",
                "To list your property, you'll need to provide basic details and photos. Shall I walk you through the process?",
                "Selling on Nextopson is commission-free! Would you like to know more about our listing process?"
            ],
            "context_set": "property_listing"
        },
        {
            "tag": "pricing",
            "patterns": [
                "What are the charges",
                "How much do you charge",
                "Fees",
                "Commission",
                "Cost of listing",
                "Pricing",
                "Service charges",
                "Is it free"
            ],
            "responses": [
                "Nextopson operates on a zero-brokerage model. We don't charge any commission or hidden fees!",
                "Our service is completely free! No brokerage, no hidden charges.",
                "We don't charge any fees or commission. Our platform is free for both buyers and sellers.",
                "Using Nextopson is 100% free. We believe in making real estate transactions cost-effective."
            ],
            "context_set": ""
        },
        {
            "tag": "verification",
            "patterns": [
                "How do you verify properties",
                "Property verification",
                "Are listings genuine",
                "Verification process",
                "How to trust listings",
                "Are properties verified"
            ],
            "responses": [
                "We verify all property listings through:\n1. Document verification\n2. Owner authentication\n3. Physical verification\n4. Legal checks",
                "Every listing undergoes strict verification including document checks and owner authentication.",
                "Our team personally verifies each property to ensure authenticity and prevent fraud.",
                "We have a robust verification system to ensure all listings are genuine and accurate."
            ],
            "context_set": ""
        },
        {
            "tag": "typo_property_search",
            "patterns": [
                "proprty in mumbai",
                "2bhk flat in begaluru",
                "cheap flat in pune neer IT park",
                "propertys for sale",
                "hous for rent in hyderbad",
                "3 BHK in chenai",
                "affortable apartment",
                "low budget propertys"
            ],
            "responses": [
                "No worries about typos! Let's help you find the right property. Did you mean a property in Bangalore or Mumbai?",
                "I think I understand what you're looking for. Let me help you find properties matching your requirements.",
                "We'll find your perfect property, spelling mistakes and all!"
            ],
            "context_set": "typo_search"
        },
        {
            "tag": "contact",
            "patterns": [
                "How do I contact support",
                "Contact number",
                "Email address",
                "Help desk",
                "Customer service",
                "Support contact",
                "Need help"
                "How do I contact support?"
            ],
            "responses": [
                "You can reach us through:\n1. Email: support@nextopson.com\n2. Phone: 1800-XXX-XXXX\n3. Live chat on our website\n4. Help center",
                "Our support team is available 24/7. Would you like our contact details?",
                "Need assistance? You can reach us via email, phone, or live chat.",
                "We're here to help! How would you like to contact our support team?"
            ],
            "context_set": ""
        },
        {
            "tag": "typo_property_search",
            "patterns": [
                "proprty in mumbai",
                "2bhk flat in begaluru",
                "cheap flat in pune neer IT park",
                "propertys for sale",
                "hous for rent in hyderbad",
                "3 BHK in chenai",
                "affortable apartment",
                "low budget propertys"
            ],
            "responses": [
                "No worries about typos! Let's help you find the right property. Did you mean a property in Bangalore or Mumbai?",
                "I think I understand what you're looking for. Let me help you find properties matching your requirements.",
                "We'll find your perfect property, spelling mistakes and all!"
            ],
            "context_set": "typo_search"
        },
        {
            "tag": "advanced_property_types",
            "patterns": [
                "I want a luxury villa",
                "Looking for a penthouse",
                "Commercial property needed",
                "Agricultural land for sale",
                "Investment property options",
                "Farmhouse available?",
                "Duplex apartments",
                "Luxury villa chahiye",
                "Farmhouse ki talash",
                "Commercial space dekh rahe hain"
            ],
            "responses": [
                "We have an extensive range of property types. From luxury villas to commercial spaces, we've got it all!",
                "Explore our diverse property portfolio including penthouses, farmhouses, and investment properties.",
                "Apki har property need ke liye hum ready hain! Luxury se commercial, sab kuch available!",
                "Specific property type chahiye? Hamara inventory bahut comprehensive hai!"
            ],
            "context_set": "advanced_property"
        },
        {
            "tag": "legal_documentation",
            "patterns": [
                "Property papers kaise check karoon?",
                "How to verify property documents?",
                "Legal verification process",
                "Document verification steps",
                "Clear property title chahiye",
                "Property ke legal issues",
                "How safe is the property legally?"
            ],
            "responses": [
                "Our comprehensive legal verification includes:\n1. Title search\n2. Document authentication\n3. No-objection certificate check\n4. Legal compliance assessment",
                "Tension mat lo! We provide end-to-end legal document verification.",
                "Legal security is our priority. Complete documentation check guaranteed!",
                "Apke property ke legal matters mein 100% transparency!"
            ],
            "context_set": "legal_verification"
        },
        {
            "tag": "investment_advice",
            "patterns": [
                "Best areas for property investment",
                "Property investment tips",
                "Where to invest in real estate?",
                "Investment potential kaise check karoon?",
                "High return areas",
                "Real estate investment strategies",
                "Rental income potential"
            ],
            "responses": [
                "Top investment areas include: Bangalore Tech Corridor, Hyderabad's HITEC City, Mumbai's Suburban Zones, and Pune's IT Hubs.",
                "Investment strategy depends on:\n1. Location\n2. Property type\n3. Budget\n4. Future development plans",
                "Hamari team provides data-driven investment insights for maximum returns!",
                "Real estate investment mein smart move ke liye hum always ready!"
            ],
            "context_set": "investment_guidance"
        },
        {
            "tag": "nri_property",
            "patterns": [
                "NRI property purchase",
                "Foreign return property",
                "Property for NRIs",
                "How can NRIs buy in India?",
                "NRI investment rules",
                "Overseas buyer process",
                "NRI ke liye property options"
            ],
            "responses": [
                "Special NRI property services:\n1. Remote documentation\n2. Virtual property tours\n3. Legal compliance guidance\n4. Investment advisory",
                "NRIs can invest seamlessly through our dedicated international support team!",
                "Overseas property purchase made simple! Complete end-to-end support.",
                "NRI property purchase mein hassle-free experience guaranteed!"
            ],
            "context_set": "nri_property"
        },
        {
            "tag": "property_valuation",
            "patterns": [
                "Property value kaise pata chalega?",
                "How to estimate property price?",
                "Current market rate",
                "Property valuation methods",
                "Sahi rate kaise determine karoon?",
                "Market value assessment",
                "Fair price evaluation"
            ],
            "responses": [
                "Our valuation process includes:\n1. Comparative market analysis\n2. Location assessment\n3. Property condition evaluation\n4. Future growth potential",
                "Get instant property valuation with our AI-powered pricing tool!",
                "Scientific valuation method se exact market value jaan sakte hain!",
                "Transparent, data-driven property pricing ke saath bilkul sahi deal!"
            ],
            "context_set": "property_valuation"
        },
        {
            "tag": "tech_integration",
            "patterns": [
                "Virtual property tour",
                "3D property visualization",
                "Online property booking",
                "Tech-enabled real estate",
                "Digital property search",
                "Tech solutions in property",
                "Smart property platform"
            ],
            "responses": [
                "Advanced tech features:\n1. AI-powered matching\n2. Virtual 3D tours\n3. Digital documentation\n4. Real-time property alerts",
                "Technology meets real estate - seamless, efficient, transparent!",
                "Digital platform se property search kabhi itni aasaan nahi thi!",
                "Tech-driven solutions for modern property seekers!"
            ],
            "context_set": "tech_solutions"
        },
        {
            "tag": "eco_friendly_properties",
            "patterns": [
                "Green building options",
                "Sustainable property",
                "Eco-friendly housing",
                "Energy-efficient homes",
                "Green certification",
                "Sustainable living spaces",
                "Environmentally friendly property"
            ],
            "responses": [
                "Eco-friendly properties with:\n1. Solar integration\n2. Rainwater harvesting\n3. Energy-efficient design\n4. Green certifications",
                "Sustainable living ke liye perfect properties! Environment-friendly solutions!",
                "Green living spaces that combine comfort and sustainability!",
                "Environmentally conscious property options for modern buyers!"
            ],
            "context_set": "eco_property"
        },
        {
            "tag": "financial_support",
            "patterns": [
                "Home loan help",
                "Mortgage options",
                "Bank financing",
                "Home loan ke liye guidance",
                "Property ke liye loan",
                "How to get property loan?"
            ],
            "responses": [
                "We partner with top banks for home loan support. Get pre-approved faster!",
                "Loan process simplified: 1) Credit check 2) Document verification 3) Bank approval",
                "Apke property dream ke liye financial solutions ready!"
            ],
            "context_set": "loan_support"
        },
        {
            "tag": "rental_agreement",
            "patterns": [
                "Rental agreement template",
                "How to make rental contract?",
                "Rent agreement formats",
                "Legal rental document",
                "Rent agreement banane ke steps"
            ],
            "responses": [
                "Comprehensive rental agreement services:\n1. Template creation\n2. Legal verification\n3. E-registration support",
                "Standard and customized rental agreement solutions available!",
                "Rent agreement mein zero confusion guarantee!"
            ],
            "context_set": "legal_docs"
        },
        {
            "tag": "property_insurance",
            "patterns": [
                "Property insurance",
                "Home insurance plans",
                "Property protection",
                "Risk coverage for property",
                "Insurance ke options"
            ],
            "responses": [
                "Comprehensive property insurance covering:\n1. Structural damage\n2. Natural calamities\n3. Theft protection",
                "Apki property ki complete security humare saath!",
                "Multiple insurance plans tailored to your property needs!"
            ],
            "context_set": "insurance_support"
        },
        {
            "tag": "property_maintenance",
            "patterns": [
                "Property maintenance services",
                "Home repair support",
                "Renovation guidance",
                "Maintenance contractors",
                "Property upkeep solutions"
            ],
            "responses": [
                "End-to-end property maintenance:\n1. Regular inspections\n2. Repair services\n3. Renovation support",
                "Professional maintenance team ready to support!",
                "Property ko top condition mein rakhne ke liye complete solution!"
            ],
            "context_set": "maintenance"
        },
        {
            "tag": "property_tax",
            "patterns": [
                "Property tax calculation",
                "Tax benefits in real estate",
                "How to save on property tax?",
                "Property tax exemptions",
                "Tax planning for property"
            ],
            "responses": [
                "Comprehensive tax advisory:\n1. Tax calculation\n2. Exemption identification\n3. Investment strategies",
                "Maximum tax benefits ke liye expert guidance!",
                "Smart property investment through tax optimization!"
            ],
            "context_set": "tax_planning"
        },
        {
            "tag": "international_property",
            "patterns": [
                "Buying property abroad",
                "International real estate",
                "Global property investment",
                "Foreign property options",
                "Overseas real estate guide"
            ],
            "responses": [
                "Global property investment support across multiple countries!",
                "International real estate ke liye complete guidance and documentation!",
                "Overseas property purchase made simple and secure!"
            ],
            "context_set": "global_property"
        },
        {
            "tag": "co_ownership",
            "patterns": [
                "Property co-ownership",
                "Joint property purchase",
                "Shared property investment",
                "Co-ownership legal aspects",
                "Multiple owner property"
            ],
            "responses": [
                "Comprehensive co-ownership solutions:\n1. Legal documentation\n2. Investment structuring\n3. Risk management",
                "Multiple investors ke liye smooth property investment model!",
                "Secure and transparent co-ownership strategies!"
            ],
            "context_set": "joint_ownership"
        },
        {
            "tag": "property_development",
            "patterns": [
                "Land development",
                "Property construction guide",
                "How to develop land?",
                "Construction project management",
                "Land use optimization"
            ],
            "responses": [
                "End-to-end property development support:\n1. Feasibility study\n2. Permit acquisition\n3. Construction management",
                "Your land, maximum potential - guaranteed!",
                "Professional development strategies for optimal land use!"
            ],
            "context_set": "land_development"
        },
        {
            "tag": "distress_sale",
            "patterns": [
                "Distress property sale",
                "Urgent property selling",
                "Quick property liquidation",
                "Selling under pressure",
                "Fastest property sale"
            ],
            "responses": [
                "Quick sale solutions with maximum value protection!",
                "Distress sale ke liye specialized support team!",
                "Fastest and most secure property liquidation strategies!"
            ],
            "context_set": "urgent_sale"
        },
        {
            "tag": "retirement_property",
            "patterns": [
                "Retirement home options",
                "Senior living properties",
                "Retirement investment",
                "Elderly friendly housing",
                "Retirement community"
            ],
            "responses": [
                "Specialized retirement property solutions:\n1. Accessibility design\n2. Healthcare proximity\n3. Community living",
                "Comfortable and secure retirement living options!",
                "Senior citizens ke liye perfect property solutions!"
            ],
            "context_set": "retirement_living"
        },
         {
            "tag": "property_crowdfunding",
            "patterns": [
                "Real estate crowdfunding",
                "Collective property investment",
                "Fractional property ownership",
                "Group property investment",
                "Crowd investment in real estate"
            ],
            "responses": [
                "Innovative crowdfunding models:\n1. Minimum investment options\n2. Diversified property portfolio\n3. Transparent returns",
                "Collective investment se maximum potential!",
                "Low-entry real estate investment solutions!"
            ],
            "context_set": "investment_crowdfunding"
        },
        {
            "tag": "heritage_property",
            "patterns": [
                "Historic property restoration",
                "Heritage building purchase",
                "Antique property restoration",
                "Historical property investment",
                "Conservation property"
            ],
            "responses": [
                "Specialized heritage property support:\n1. Legal compliance\n2. Restoration guidance\n3. Cultural preservation",
                "Historical properties ke liye comprehensive solutions!",
                "Preserve history, invest smartly!"
            ],
            "context_set": "heritage_conservation"
        },
        {
            "tag": "startup_workspace",
            "patterns": [
                "Startup office space",
                "Co-working property",
                "Shared workspace options",
                "Flexible office solutions",
                "Startup friendly locations"
            ],
            "responses": [
                "Startup workspace solutions:\n1. Flexible lease terms\n2. Tech-enabled spaces\n3. Networking opportunities",
                "Startups ke liye perfect workspace solutions!",
                "Innovative office spaces for modern entrepreneurs!"
            ],
            "context_set": "workspace_solutions"
        },
        {
            "tag": "property_foreclosure",
            "patterns": [
                "Foreclosure property",
                "Bank auction properties",
                "Distressed real estate",
                "Foreclosure investment",
                "Auction property purchase"
            ],
            "responses": [
                "Foreclosure property support:\n1. Auction listings\n2. Legal verification\n3. Investment potential assessment",
                "Risky properties mein smart investment strategies!",
                "Comprehensive foreclosure property guidance!"
            ],
            "context_set": "foreclosure_market"
        },
        {
            "tag": "student_housing",
            "patterns": [
                "Student accommodation",
                "Hostel property",
                "University area housing",
                "Student friendly rentals",
                "Campus proximity properties"
            ],
            "responses": [
                "Student housing solutions:\n1. Safety-first properties\n2. Affordable options\n3. Proximity to educational institutions",
                "Students ke liye perfect living spaces!",
                "Comfortable and secure student accommodation!"
            ],
            "context_set": "student_living"
        },
        {
            "tag": "agricultural_land",
            "patterns": [
                "Farm land purchase",
                "Agricultural property investment",
                "Rural property options",
                "Land for farming",
                "Agricultural zone properties"
            ],
            "responses": [
                "Agricultural land solutions:\n1. Soil quality assessment\n2. Legal documentation\n3. Investment potential",
                "Farming ke liye perfect land options!",
                "Agricultural property investment made simple!"
            ],
            "context_set": "agricultural_investment"
        },
        {
            "tag": "green_zone_property",
            "patterns": [
                "Eco-friendly zones",
                "Green belt properties",
                "Environmentally protected areas",
                "Sustainable living locations",
                "Conservation zone properties"
            ],
            "responses": [
                "Green zone property solutions:\n1. Environmental compliance\n2. Sustainability certification\n3. Conservation guidelines",
                "Environment ke saath investment!",
                "Sustainable property options for conscious buyers!"
            ],
            "context_set": "green_property"
        },
        {
            "tag": "digital_nomad_housing",
            "patterns": [
                "Remote work housing",
                "Flexible location properties",
                "Digital nomad friendly spaces",
                "Work from anywhere housing",
                "Nomadic lifestyle properties"
            ],
            "responses": [
                "Digital nomad housing solutions:\n1. High-speed internet\n2. Flexible lease terms\n3. Global location options",
                "Work anywhere, live everywhere!",
                "Modern lifestyle ke liye perfect properties!"
            ],
            "context_set": "nomad_living"
        },
        {
            "tag": "luxury_amenities",
            "patterns": [
                "High-end property features",
                "Luxury housing amenities",
                "Premium property options",
                "Exclusive housing facilities",
                "Ultra-luxury properties"
            ],
            "responses": [
                "Luxury property features:\n1. Smart home technology\n2. Premium locations\n3. Exclusive amenities",
                "Luxury living ke liye ultimate solutions!",
                "Premium properties with world-class amenities!"
            ],
            "context_set": "premium_housing"
        },
        {
            "tag": "micro_housing",
            "patterns": [
                "Compact living spaces",
                "Micro apartments",
                "Minimalist housing",
                "Small space solutions",
                "Efficient compact properties"
            ],
            "responses": [
                "Micro housing solutions:\n1. Space optimization\n2. Cost-effective options\n3. Urban living design",
                "Small spaces, big potential!",
                "Efficient living ke liye smart property options!"
            ],
            "context_set": "compact_living"
        },
        {
            "tag": "typo_property_search",
            "patterns": [
                "proprty in mumbai",
                "2bhk flat in begaluru",
                "cheap flat in pune neer IT park",
                "propertys for sale",
                "hous for rent in hyderbad",
                "3 BHK in chenai",
                "affortable apartment",
                "low budget propertys"
            ],
            "responses": [
                "No worries about typos! Let's help you find the right property. Did you mean a property in Bangalore or Mumbai?",
                "I think I understand what you're looking for. Let me help you find properties matching your requirements.",
                "We'll find your perfect property, spelling mistakes and all!"
            ],
            "context_set": "typo_search"
        },
        {
            "tag": "conversational_mistakes",
            "patterns": [
                "i want flat",
                "where house?",
                "give me proprty",
                "show flats",
                "want to bye house",
                "sell my home fast",
                "how much cost",
                "wat is price"
            ],
            "responses": [
                "I'll help you find exactly what you're looking for! Can you provide more details about the property you want?",
                "No problem! Let's clarify your property requirements step by step.",
                "We'll decode your property needs, no matter how they're expressed!"
            ],
            "context_set": "casual_search"
        },
        {
            "tag": "mixed_language_search",
            "patterns": [
                "2 BHK flat in Bangalore mein kitne ka milega",
                "cheap property near office ke paas",
                "rent ke liye apartment chahiye",
                "sell my flat fast mein",
                "property value kya hai bro",
                "investment property for returns"
            ],
            "responses": [
                "Bilingual search? No problem! Let's find your perfect property.",
                "I understand your mixed-language query. Tell me more about what you're looking for.",
                "Combining languages shows your unique style! Let's find your ideal property."
            ],
            "context_set": "mixed_language"
        },
        {
            "tag": "emotional_search",
            "patterns": [
                "plz help me find home",
                "urgent!!! need flat",
                "cheap property asap",
                "im desperate for house",
                "need home badly",
                "help me fast",
                "quick property solution"
            ],
            "responses": [
                "We understand your urgency. Let's find the right property for you quickly!",
                "Your property search is our top priority. Tell me more about what you need.",
                "Urgent needs, quick solutions! We're here to help you find your perfect home."
            ],
            "context_set": "urgent_search"
        },
        {
            "tag": "abbreviated_search",
            "patterns": [
                "2 bhk in mum",
                "3 bk near IT",
                "prop in blr",
                "rent in hyd",
                "sell in del",
                "buy in pune",
                "invest in ch"
            ],
            "responses": [
                "Got your abbreviated search! Let me help you find properties in full.",
                "City abbreviations? We'll decode and find your perfect property!",
                "Quick searches welcome! Let's expand your property hunt."
            ],
            "context_set": "abbreviated_search"
        },
        {
            "tag": "budget_confusion",
            "patterns": [
                "10 lak budget property",
                "20 lakh flat",
                "cheap proprty under 50 lak",
                "budget flat in 30 lac",
                "low cost house in 15 lakhs"
            ],
            "responses": [
                "Budget-friendly options are our specialty! Let's find properties that match your budget.",
                "Great budget range! We'll help you find the best property value.",
                "Budget constraints? We'll find the perfect match for your investment."
            ],
            "context_set": "budget_search"
        },
        {
            "tag": "informal_requirements",
            "patterns": [
                "need big house",
                "want nice flat",
                "looking for good property",
                "awesome apartment",
                "cool house near metro"
            ],
            "responses": [
                "Tell me more about what makes a property 'nice' or 'awesome' for you!",
                "Let's translate your informal requirements into specific property features.",
                "Your unique description helps us find the perfect property match!"
            ],
            "context_set": "informal_search"
        },
         {
            "tag": "desperate_search",
            "patterns": [
                "plz help urgant",
                "need flat immadiatly",
                "fast propertis",
                "quik rent",
                "hury up property",
                "fast sell my house"
            ],
            "responses": [
                "We're ready to help you find a property quickly! Tell me more about your urgent needs.",
                "Urgent searches are our specialty. Let's find your property fast!",
                "Quick solutions for your immediate property requirements!"
            ],
            "context_set": "urgent_search"
        },
        {
            "tag": "budget_broken_english",
            "patterns": [
                "i want proprty 10 lac",
                "budget 20 lak flat",
                "cheep house 15 lakh",
                "low cost propertys",
                "how much 3 bhk cost",
                "rent kitna hoga"
            ],
            "responses": [
                "Budget-friendly options are our strength! Let's find a property that fits your budget.",
                "I understand your budget range. We'll help you find the perfect match!",
                "Your budget is our priority. Let's explore affordable options!"
            ],
            "context_set": "budget_search"
        },
        {
            "tag": "location_confusion",
            "patterns": [
                "flat in mumbai neer station",
                "propertys in bangalor it area",
                "house in pune nir office",
                "rent in hyderbad",
                "propertys close 2 metro"
            ],
            "responses": [
                "Location is key! Let's find properties in the right area for you.",
                "I'll help you find properties near your preferred location.",
                "Proximity matters! Tell me more about the specific area you want."
            ],
            "context_set": "location_search"
        },
        {
            "tag": "emotional_property_need",
            "patterns": [
                "i am desparate for home",
                "plz help me find flat",
                "need house asap",
                "urgent proprty needed",
                "help me buy home",
                "want to sell fast"
            ],
            "responses": [
                "We understand your urgency. Let's find the right property quickly!",
                "Your housing needs are our top priority. How can we help?",
                "Urgent property solutions start right here!"
            ],
            "context_set": "emotional_search"
        },
        {
            "tag": "mixed_requirement",
            "patterns": [
                "2 bhk flat mein kitna",
                "cheap property near office",
                "rent ke liye apartment",
                "investment property returns",
                "how much 3 bhk cost"
            ],
            "responses": [
                "Mixed requirements? No problem! Let's break down your property needs.",
                "I'll help you find a property that matches your specific criteria.",
                "Your unique property search starts now!"
            ],
            "context_set": "mixed_search"
        },
        {
            "tag": "super_casual_search",
            "patterns": [
                "yo property",
                "wassup flat",
                "any good house?",
                "cheap stuff",
                "cool apartment plz",
                "help me bro"
            ],
            "responses": [
                "Hey there! Let's find your perfect property.",
                "Cool requirements! Tell me more about what you're looking for.",
                "We speak your language! What's your ideal property?"
            ],
            "context_set": "casual_search"
        },
        {
            "tag": "abbreviation_nightmare",
            "patterns": [
                "2 bk in blr",
                "3 bhk mum",
                "rent in hyd",
                "prop del",
                "buy pune",
                "sell ch"
            ],
            "responses": [
                "City abbreviations decoded! Let's find your perfect property.",
                "Got your shorthand search! We'll expand and find your ideal home.",
                "Quick searches welcome! Tell me more about what you want."
            ],
            "context_set": "abbreviated_search"
        },
        {
            "tag": "greeting",
            "patterns": [
                "hi ther!",
                "hey bot r u?",
                "helloooo",
                "hiii",
                "wassup nxtopson",
                "hey help me",
                "any 1 dere?",
                "yo propety bot!",
                "helppp"
            ],
            "responses": [
                "Hello! Welcome to Nextopson. How can I help you with property needs?",
                "Hi there! Looking to buy, sell, or rent?",
                "Welcome! What property assistance do you need?"
            ],
            "context_set": ""
        },
        {
            "tag": "goodbye",
            "patterns": [
                "bye byee",
                "gtg",
                "c ya",
                "tata",
                "laters",
                "bye bottt",
                "kthxbye",
                "im out"
            ],
            "responses": [
                "Thank you for using Nextopson! Have a great day!",
                "Goodbye! Return anytime for property help.",
                "See you later! We're always here for real estate needs."
            ],
            "context_set": ""
        },
        {
            "tag": "property_search",
            "patterns": [
                "i want proprty",
                "show me hous",
                "serach flat",
                "need 2 buy home",
                "wats availble?",
                "find me cheep flat",
                "any houses neer me?"
            ],
            "responses": [
                "What type of property are you looking for? Location and budget?",
                "Help me understand your property requirements.",
                "I'll assist you in finding the right property."
            ],
            "context_set": "property_search"
        },
        {
            "tag": "property_listing",
            "patterns": [
                "sell my prprty",
                "how 2 list",
                "want 2 sell hous",
                "list my flat",
                "put propertys on market",
                "want 2 advertse"
            ],
            "responses": [
                "Listing is easy:\n1. Create account\n2. Click 'List Property'\n3. Add details\n4. Upload photos\n5. Submit",
                "Zero-brokerage listing process available!",
                "I'll guide you through property listing."
            ],
            "context_set": "property_listing"
        },
        {
            "tag": "pricing",
            "patterns": [
                "wats charges?",
                "any fees?",
                "how much 2 list",
                "is dis free?",
                "hidden costs?",
                "pay kitna?"
            ],
            "responses": [
                "Zero-brokerage model. No commission or hidden fees!",
                "Our service is 100% free.",
                "No charges for buyers or sellers."
            ],
            "context_set": ""
        },
        {
            "tag": "verification",
            "patterns": [
                "r listings real?",
                "how u check propertys?",
                "trust worthi?",
                "legit or not?",
                "verify kaise?"
            ],
            "responses": [
                "Verification steps:\n1. Document check\n2. Owner authentication\n3. Physical verification\n4. Legal checks",
                "We personally verify each property.",
                "Robust system to ensure genuine listings."
            ],
            "context_set": ""
        },
        {
            "tag": "contact",
            "patterns": [
                "how 2 contact?",
                "suport number?",
                "need help plz",
                "wats email?",
                "tell me contact"
            ],
            "responses": [
                "Contact us:\n1. Email: support@nextopson.com\n2. Phone: 1800-XXX-XXXX\n3. Live chat\n4. Help center",
                "24/7 support available.",
                "Multiple ways to reach us!"
            ],
            "context_set": ""
        }
    ]
}