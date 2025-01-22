# Import logging.config explicitly
import logging
import logging.config
import re
import string
import random
import json
from datetime import datetime
import nltk
from nltk.chat.util import Chat, reflections
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from collections import defaultdict
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from config import BOT_CONFIG, LOGGING_CONFIG
from intents import intents
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer




LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'nextopson_bot.log',
            'mode': 'a'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NextopsonSupportBot:
    def __init__(self):
        # Initialize conversation memory
        self.conversation_memory = defaultdict(list)
        self.memory_size = 5
        self.MAX_MEMORY_SIZE = 1000
        self.SESSION_TIMEOUT = 3600  # 1 hour

        self.intents = intents['intents']
        self.conversation_flow = ConversationFlow()


        self.train_data = [
            # Basic Information
            ('What is Nextopson?', 'Nextopson is a zero-brokerage real estate platform that directly connects property buyers and sellers. We make property transactions simple and cost-effective.'),
            ('How does Nextopson work?', 'Nextopson lets you list and find properties without any brokerage fees. Simply sign up, browse listings, or post your property to get started.'),
            ('Why choose Nextopson?', 'Nextopson offers zero brokerage, direct buyer-seller connection, verified listings, and a hassle-free property transaction experience.'),
            
            # Property Listing
            ('How do I list my property?', 'To list your property on Nextopson: 1) Sign up/Login 2) Click "Post Property" 3) Fill in property details 4) Upload photos 5) Submit for verification. Need help with any step?'),
            ('What details do I need to list?', 'You\'ll need to provide property location, type, size, price, amenities, and high-quality photos. Would you like a detailed listing guide?'),
            ('How long does listing take?', 'Property listing takes just 10-15 minutes. Our verification process typically completes within 24 hours.'),
            
            # Property Search
            ('How to search properties?', 'Use our search filters to find properties by location, type, budget, and amenities. You can also save searches and get alerts for new matches.'),
            ('Can I save properties?', 'Yes! Create a free account to save favorite properties, set alerts, and track property updates.'),
            ('How to contact sellers?', 'Click "Contact Seller" on any listing to send a message or request property details directly through our platform.'),
            
            # Fees and Pricing
            ('What are the fees?', 'Nextopson is completely free! We charge zero brokerage and no hidden fees for listing or searching properties.'),
            ('Is there any commission?', 'No commission at all! Nextopson operates on a zero-brokerage model to make property transactions more affordable.'),
            ('Are there premium services?', 'All our core services are free. We may offer optional premium features for enhanced visibility in the future.'),
            
            # Safety and Verification
            ('Are listings verified?', 'Yes, our team verifies all property listings to ensure authenticity. We check property documents and seller credentials.'),
            ('Is it safe to use Nextopson?', 'Absolutely! We verify all listings, secure your data, and facilitate safe communication between buyers and sellers.'),
            ('How to report issues?', 'Use the "Report" button on listings or contact our support team through the help center for immediate assistance.'),
            
            # Account Management
            ('How to create account?', 'Click "Sign Up" on nextopson.com, enter your details, verify your email, and start using our services immediately.'),
            ('Edit my listing', 'Log in to your account, go to "My Listings," select the property, and click "Edit" to update any information.'),
            ('Delete my listing', 'Access "My Listings" in your account, find the property, and use the "Delete Listing" option to remove it.'),
            
            # Support
            ('Contact support', 'You can reach our support team through: 1) Help Center 2) support@nextopson.com 3) In-app chat 4) Customer care number.'),
            ('Technical issues', 'For technical issues, please try refreshing the page or clearing your browser cache. If the problem persists, contact our support team.'),
            ('Forgot password', 'Click "Forgot Password" on the login page, enter your registered email, and follow the reset instructions sent to you.'),
            
            # Documents
            ('Required documents', 'For listing: Property ownership proof, tax receipts, and ID proof. For buying: Just create an account to start viewing properties.'),
            ('Document verification', 'Our team verifies all property documents within 24 hours of submission to ensure authenticity.'),
            ('Update documents', 'Log in, go to "My Listings," select your property, and use the "Update Documents" option to add or modify documents.'),
            
            # Navigation
            ('Find my listings', 'After logging in, click on "My Account" and select "My Listings" to view all your property listings.'),
            ('View saved properties', 'Access your saved properties through "My Account" → "Favorites" after logging in.'),
            ('Search filters', 'Use our advanced filters for location, property type, price range, amenities, and more to find your perfect property.'),
            
            # Property Transaction
            ('How to buy property?', 'Browse listings, contact sellers directly, negotiate, and proceed with documentation. Our team can guide you through each step.'),
            ('Payment process', 'Payments are handled directly between buyers and sellers. We recommend secure payment methods and can provide guidance on the process.'),
            ('Property inspection', 'Schedule property visits directly with sellers through our platform. We recommend thorough inspection before proceeding.'),

            # New Additional Training Data
            
            # Mobile App
            ('Is there a mobile app?', 'Yes, Nextopson is available on both iOS and Android. Download our app to search properties and manage listings on the go.'),
            ('App features', 'Our mobile app offers property search, instant notifications, chat with sellers/buyers, and easy listing management.'),
            ('App not working', 'Try updating the app to the latest version, check your internet connection, or clear the app cache. Contact support if issues persist.'),
            
            # Virtual Services
            ('Virtual tour', 'Many properties offer virtual tours. Look for the "360° View" icon on listings to explore properties virtually.'),
            ('Online documentation', 'You can upload and verify documents online through our secure platform. We accept digital signatures for most documents.'),
            ('Video calling', 'Use our built-in video calling feature to have virtual meetings with property owners or buyers.'),
            
            # Property Types
            ('Types of properties', 'We list residential properties (apartments, houses, villas), commercial spaces (offices, shops), and land/plots.'),
            ('Residential options', 'Browse apartments, independent houses, villas, penthouses, studio apartments, and more in our residential section.'),
            ('Commercial properties', 'Find offices, retail spaces, warehouses, industrial properties, and commercial land in our commercial section.'),
            
            # Location Based
            ('Popular locations', 'View trending localities, upcoming areas, and premium locations in your city with our location guides.'),
            ('Nearby amenities', 'Each listing shows nearby schools, hospitals, markets, and public transport options within a 5km radius.'),
            ('Area guides', 'Access detailed area guides with information about locality, infrastructure, prices, and future development plans.'),
            
            # Pricing and Loans
            ('Price negotiation', 'You can negotiate directly with sellers through our platform. We provide price trends to help make informed decisions.'),
            ('Home loans', 'Compare home loan offers from multiple banks through our platform. We have partnered with leading financial institutions.'),
            ('EMI calculator', 'Use our EMI calculator to estimate monthly payments based on loan amount, interest rate, and tenure.'),
            
            # Legal
            ('Legal verification', 'We help verify property legal status and documentation. Optional legal assistance is available through our partner lawyers.'),
            ('Property ownership', 'We verify property ownership and ensure all listings have clear titles before they go live on our platform.'),
            ('Legal documents', 'Get guidance on required legal documents like sale deed, property tax receipts, NOC, and occupancy certificate.'),
            
            # Premium Features
            ('Featured listing', 'Boost your property visibility with our featured listing option. Your property appears at the top of search results.'),
            ('Premium membership', 'Premium members get priority support, advanced analytics, and exclusive access to pre-launch properties.'),
            ('Marketing services', 'We offer professional photography, 3D tours, and social media promotion for premium listings.'),
            
            # Rental Properties
            ('Rental listing', 'List your property for rent with detailed terms, preferred tenant profile, and rental agreement requirements.'),
            ('Tenant verification', 'We offer tenant verification services including background checks and document verification.'),
            ('Rental agreement', 'Access standard rental agreement templates or get customized agreements through our legal partners.'),
            
            # Investment
            ('Investment advice', 'Our market insights and property analytics help you make informed investment decisions.'),
            ('ROI calculator', 'Calculate potential returns on your property investment using our ROI calculator tool.'),
            ('Market trends', 'Access real-time market trends, price history, and future projections for different localities.'),
            
            # Additional Services
            ('Interior design', 'Connect with our partner interior designers for home renovation and decoration services.'),
            ('Packers and movers', 'Book verified packers and movers through our platform for hassle-free relocation.'),
            ('Property management', 'Our property management services help you maintain and manage your property remotely.'),
            
            # Support Queries
            ('Response time', 'We typically respond to queries within 2 hours during business hours (9 AM - 6 PM).'),
            ('Feedback', 'Share your feedback through our app/website or email us at feedback@nextopson.com'),
            ('File complaint', 'Report issues or file complaints through our grievance redressal system for quick resolution.')
        ]

 




        # Complete conversation patterns
        self.pairs = [
            ('hello|hi|hey|hii|hiiii|hlo|howdy|greetings', [
                'Welcome to Nextopson support! How can I assist you today?',
                'Hello! How may I help you with your property needs?',
                'Hi! Looking to buy, sell, or need help with Nextopson?',
                'Greetings! How can I make your property journey easier today?'
            ]),
            
            ('bye|goodbye|see you|cya|good night|good morning', [
                'Thank you for choosing Nextopson! Feel free to return if you need more assistance.',
                'Have a great day! We\'re here 24/7 for your property needs.',
                'Goodbye! Don\'t hesitate to contact us for any property-related help.',
                'Take care! Remember, we\'re always here to help with your property needs.'
            ]),
            ('thanks|thank you|thx|thankyou|appreciate', [
                'You\'re welcome! Let us know if you need anything else.',
                'Happy to help! Feel free to reach out for any property-related queries.',
                'Glad to assist! Don\'t hesitate to ask if you have more questions.',
                'It\'s my pleasure! Your satisfaction is our priority at Nextopson.'
            ]),
            ('help|support|assistance', [
                'I\'m here to help! What specific assistance do you need with Nextopson?',
                'How can I assist you today with your property needs?',
                'I\'d be happy to help. What would you like to know about our services?'
            ]),
            ('property|properties|listing|listings', [
                'Would you like to browse properties or list your own on Nextopson?',
                'I can help you with property listings. Are you interested in buying or selling?',
                'Let me guide you through our property services. What are you looking for?'
            ])
        ]
       
        
        # Initialize patterns
        self.sentiment_patterns = {
            'positive': r'\b(great|awesome|excellent|good|wonderful|fantastic|thank|thanks|helpful)\b',
            'negative': r'\b(bad|poor|terrible|awful|horrible|worst|useless|waste|frustrated)\b',
            'urgent': r'\b(urgent|asap|emergency|immediately|quick|hurry)\b'
        }
        
        self.property_types = {
            'residential': r'\b(house|apartment|flat|villa|condo|residential|1bhk|2bhk|3bhk)\b',
            'commercial': r'\b(office|shop|retail|commercial|warehouse|store)\b',
            'land': r'\b(plot|land|acre|vacant|empty)\b'
        }
        
        self.location_patterns = r'\b(near|location|area|city|locality|address)\b'
        self.price_patterns = r'\b(price|cost|budget|expensive|cheap|affordable)\b'

        # Initialize NLTK
        try:
            nltk.download('punkt', quiet=True)
            nltk.download('wordnet', quiet=True)
            nltk.download('stopwords', quiet=True)
            self.stop_words = set(stopwords.words('english'))
            self.lemmatizer = WordNetLemmatizer()
        except Exception as e:
            logger.error(f"NLTK initialization error: {str(e)}")
            self.stop_words = set()
            self.lemmatizer = None

        # Initialize model and chat
        self.initialize_model()
        self.pairs = [
 ('hello|hi|hey|hii|hiiii|hlo|howdy|greetings', [
                'Welcome to Nextopson support! How can I assist you today?',
                'Hello! How may I help you with your property needs?',
                'Hi! Looking to buy, sell, or need help with Nextopson?',
                'Greetings! How can I make your property journey easier today?'
            ]),
            
            ('bye|goodbye|see you|cya|good night|good morning', [
                'Thank you for choosing Nextopson! Feel free to return if you need more assistance.',
                'Have a great day! We\'re here 24/7 for your property needs.',
                'Goodbye! Don\'t hesitate to contact us for any property-related help.',
                'Take care! Remember, we\'re always here to help with your property needs.'
            ]),
            ('thanks|thank you|thx|thankyou|appreciate', [
                'You\'re welcome! Let us know if you need anything else.',
                'Happy to help! Feel free to reach out for any property-related queries.',
                'Glad to assist! Don\'t hesitate to ask if you have more questions.',
                'It\'s my pleasure! Your satisfaction is our priority at Nextopson.'
            ]),
            ('help|support|assistance', [
                'I\'m here to help! What specific assistance do you need with Nextopson?',
                'How can I assist you today with your property needs?',
                'I\'d be happy to help. What would you like to know about our services?'
            ]),
            ('property|properties|listing|listings', [
                'Would you like to browse properties or list your own on Nextopson?',
                'I can help you with property listings. Are you interested in buying or selling?',
                'Let me guide you through our property services. What are you looking for?'
            ])            
            # Your existing pairs here
        ]
        self.chat = Chat(self.pairs, reflections)
        self.get_intent_response = self._get_intent_response


    def analyze_input(self, text):
        """Analyze input text for sentiment, property type, and other features"""
        analysis = {
            'sentiment': 'neutral',
            'property_type': 'general',
            'is_question': False,
            'has_location': False,
            'has_price': False
        }
        
        # Check sentiment
        for sentiment, pattern in self.sentiment_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                analysis['sentiment'] = sentiment
                break
        
        # Check property type
        for prop_type, pattern in self.property_types.items():
            if re.search(pattern, text, re.IGNORECASE):
                analysis['property_type'] = prop_type
                break
        
        # Check for questions
        analysis['is_question'] = '?' in text or any(word in text.lower() for word in ['what', 'how', 'where', 'when', 'why', 'who'])
        
        # Check for location references
        analysis['has_location'] = bool(re.search(self.location_patterns, text, re.IGNORECASE))
        
        # Check for price references
        analysis['has_price'] = bool(re.search(self.price_patterns, text, re.IGNORECASE))
        
        return analysis

    def get_property_type_response(self, property_type):
        """Generate response based on property type"""
        responses = {
            'residential': "For residential properties, we offer apartments, houses, and villas. Would you like to specify your preferences?",
            'commercial': "Our commercial listings include offices, shops, and warehouses. What type of commercial property are you looking for?",
            'land': "We have various land parcels available. Are you looking for agricultural, residential, or commercial plots?"
        }
        return responses.get(property_type, "What type of property are you interested in?")

    def _get_conversation_context(self, user_id):
        """Get recent conversation context for a user"""
        try:
            if user_id not in self.conversation_memory:
                self.conversation_memory[user_id] = []
            return self.conversation_memory[user_id][-3:] if self.conversation_memory[user_id] else []
        except Exception as e:
            logger.error(f"Error getting conversation context: {str(e)}")
            return []        

    def initialize_model(self):
        """Initialize and train the ML model"""
        try:
            # Prepare training data
            X_train = [self.preprocess_input(x[0]) for x in self.train_data]
            y_train = [x[1] for x in self.train_data]
            
            # Split data with stratification
            X_train, X_val, y_train, y_val = train_test_split(
                X_train, y_train, 
                test_size=0.2, 
                random_state=42,
                
            )
            
            # Enhanced ML Pipeline
            self.pipeline = make_pipeline(
                TfidfVectorizer(
                    ngram_range=(1, 3),
                    max_features=10000,
                    stop_words='english',
                    min_df=1,
                    max_df=0.95
                ),
                RandomForestClassifier(
                    n_estimators=100,
                    max_depth=15,
                    min_samples_split=2,
                    class_weight='balanced',
                    random_state=42
                )
            )
            
            # Train and validate
            self.pipeline.fit(X_train, y_train)
            val_pred = self.pipeline.predict(X_val)
            val_report = classification_report(y_val, val_pred, zero_division=1)
            logger.info(f"Model validation report:\n{val_report}")
            
        except Exception as e:
            logger.error(f"Model initialization error: {str(e)}")
             # Initialize a simple fallback pipeline
            self.pipeline = make_pipeline(
                TfidfVectorizer(),
                RandomForestClassifier()
            )
            # Train with minimal data
            self.pipeline.fit(['default query'], ['default response'])

    def preprocess_input(self, text):
        """Improved input preprocessing"""
        try:
            if not isinstance(text, str):
                return ""
                
            # Basic cleaning
            text = text.lower().strip()
            
            # Remove special characters while preserving important ones
            text = re.sub(r'[^\w\s?.!,@#$%&*()-]', ' ', text)
            
            # Handle multiple spaces
            text = re.sub(r'\s+', ' ', text)
            
             # NLTK processing with error handling
            if self.lemmatizer:
                try:
                    tokens = nltk.word_tokenize(text)
                    tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                            if token not in self.stop_words]
                    text = ' '.join(tokens)
                except Exception as e:
                    logger.warning(f"NLTK processing failed: {str(e)}")
                    tokens = text.split()
                    
            return text
            
        except Exception as e:
            logger.error(f"Preprocessing error: {str(e)}")
            return ""
        
    def _get_intent_response(self, user_input):
        """Get response based on intent matching"""
        user_input = user_input.lower()
        
        for intent in self.intents:
            for pattern in intent['patterns']:
                if pattern.lower() in user_input:
                    return random.choice(intent['responses'])
        
        return None

    def get_response(self, user_input, user_id='default'):
        """Enhanced response generation with better flow management"""
        try:
            # Input validation
            if not isinstance(user_input, str) or len(user_input.strip()) < 2:
                return "Could you please provide more details about your question?"

            # Check for new question indicators
            new_question_words = ['new question', 'different question', 'another question', 
                                'something else', 'different topic']
            if any(word in user_input.lower() for word in new_question_words):
                self.conversation_flow.reset_flow(user_id)
                return "I'm ready for your new question. How can I help?"

            # Check if user is in an active flow
            flow_state = self.conversation_flow.get_current_flow_state(user_id)
            if flow_state is None:
                # Normal response for new questions
                cleaned_input = self.preprocess_input(user_input)
                analysis = self.analyze_input(cleaned_input)
                context = self._get_conversation_context(user_id)

                # Check for flow triggers
                lower_input = cleaned_input.lower()
                if any(word in lower_input for word in ['buy', 'purchase', 'looking for', 'want to buy']):
                    return self.conversation_flow.start_flow('buying', user_id)
                elif any(word in lower_input for word in ['sell', 'selling', 'list property']):
                    return self.conversation_flow.start_flow('selling', user_id)

                # Use your existing response generation methods
                # 1. Try intent matching first
                intent_response = self._get_intent_response(user_input)
                if intent_response:
                    return intent_response

                # 2. Try ML model
                try:
                    ml_response, confidence = self.get_ml_response(cleaned_input)
                    if ml_response and confidence > 0.7:
                        enhanced_response = self.enhance_response(ml_response, analysis, context)
                        self._update_memory(user_id, {
                            'input': cleaned_input,
                            'response': enhanced_response,
                            'analysis': analysis,
                            'confidence': float(confidence),
                            'timestamp': datetime.now()
                        })
                        return enhanced_response
                except Exception as e:
                    logger.error(f"ML response error: {str(e)}")

                # 3. Try pattern matching
                try:
                    chat_response = self.chat.respond(cleaned_input)
                    if chat_response:
                        return chat_response
                except Exception as e:
                    logger.error(f"Chat response error: {str(e)}")

                return self.get_contextual_fallback_response(analysis)
            else:
                # Handle ongoing flow
                next_response = self.conversation_flow.get_next_response(user_id, user_input)
                if next_response:
                    return next_response
                else:
                    # Flow completed or interrupted
                    self.conversation_flow.reset_flow(user_id)
                    return "Is there anything else I can help you with?"

        except Exception as e:
            logger.error(f"Response generation error: {str(e)}")
            self.conversation_flow.reset_flow(user_id)
            return "I'm having trouble understanding your question. Could you rephrase it?"

    def _cleanup_old_sessions(self):
        """Clean up old sessions"""
        try:
            current_time = datetime.now()
            for user_id in list(self.conversation_memory.keys()):
                if len(self.conversation_memory[user_id]) > 0:
                    last_interaction = self.conversation_memory[user_id][-1].get('timestamp')
                    if last_interaction and (current_time - last_interaction).seconds > self.SESSION_TIMEOUT:
                        del self.conversation_memory[user_id]
                        
            # Remove oldest sessions if memory limit exceeded
            if len(self.conversation_memory) > self.MAX_MEMORY_SIZE:
                oldest_user = min(
                    self.conversation_memory.keys(),
                    key=lambda k: self.conversation_memory[k][-1]['timestamp'] if self.conversation_memory[k] else datetime.now()
                )
                del self.conversation_memory[oldest_user]
                
        except Exception as e:
            logger.error(f"Session cleanup error: {str(e)}")

    def get_ml_response(self, user_input):
        """Improved ML response generation"""
        try:
            prediction = self.pipeline.predict([user_input])[0]
            confidence = max(self.pipeline.predict_proba([user_input])[0])
            return prediction, float(confidence)
        except Exception as e:
            logger.error(f"ML response error: {str(e)}")
            return None, 0.0

    def enhance_response(self, base_response, analysis, context):
        """Enhance response with context and analysis"""
        if not base_response:
            return self.get_contextual_fallback_response(analysis)

        response = base_response

        # Add urgency handling
        if analysis['sentiment'] == 'urgent':
            response = "I understand this is urgent. " + response

        # Add property type specific information
        if analysis['property_type'] != 'general':
            prop_info = {
                'residential': " We have extensive residential listings that might interest you.",
                'commercial': " Our commercial section has various options for businesses.",
                'land': " We have many land parcels available for development."
            }
            response += prop_info.get(analysis['property_type'], '')

        return response

    def get_contextual_fallback_response(self, analysis):
        """Get context-aware fallback responses"""
        if analysis['is_question']:
            return "Could you provide more details about your question? I want to give you the most accurate information."
        
        if analysis['has_location']:
            return "I see you're interested in a specific location. What type of property are you looking for in that area?"
        
        if analysis['has_price']:
            return "I notice you're asking about pricing. Are you looking to buy, sell, or rent a property?"
        
        return "I'm not quite sure what you're looking for. Could you tell me more about your property needs?"

    def _update_memory(self, user_id, interaction):
        """Update conversation memory safely"""
        try:
            if not interaction.get('timestamp'):
                interaction['timestamp'] = datetime.now()
            
            self.conversation_memory[user_id].append(interaction)
            
            if len(self.conversation_memory[user_id]) > self.memory_size:
                self.conversation_memory[user_id].pop(0)
                
        except Exception as e:
            logger.error(f"Memory update error: {str(e)}")
            
    def handle_flow_interruption(self, user_input, user_id):
        """Handle interruptions in conversation flow"""
        # Check for exit commands
        if user_input.lower() in ['exit', 'quit', 'stop', 'cancel']:
            self.conversation_flow.reset_flow(user_id)
            return "I've cancelled the current process. How else can I help you?"
            
        # Check for help commands
        if user_input.lower() in ['help', 'confused', 'what now?']:
            flow_state = self.conversation_flow.get_current_flow_state(user_id)
            if flow_state:
                return f"You're currently in the process of {flow_state['flow']}. " + \
                       "You can say 'exit' to cancel this process, or continue by answering the question."
                       
        return None        
# Add these methods to the ConversationFlow class

class ConversationFlow:
    def __init__(self):
        # Define the complete conversation flows with all possible states
        self.flows = {
            'buying': {
                'start': {
                    'message': "What type of property are you looking to buy? (e.g., apartment, house, commercial)",
                    'next': 'location',
                    'validation': lambda x: bool(x.strip())
                },
                'location': {
                    'message': "Which area are you interested in?",
                    'next': 'budget',
                    'validation': lambda x: bool(x.strip())
                },
                'budget': {
                    'message': "What's your budget range?",
                    'next': 'requirements',
                    'validation': lambda x: bool(x.strip())
                },
                'requirements': {
                    'message': "Any specific requirements? (e.g., number of bedrooms, parking)",
                    'next': 'end',
                    'validation': lambda x: True  # Optional field
                },
                'end': {
                    'message': "Thank you! I'll search for properties matching your criteria. Would you like to see the available listings?",
                    'next': None
                }
            },
            'selling': {
                'start': {
                    'message': "What type of property would you like to sell?",
                    'next': 'location',
                    'validation': lambda x: bool(x.strip())
                },
                'location': {
                    'message': "Where is your property located?",
                    'next': 'price',
                    'validation': lambda x: bool(x.strip())
                },
                'price': {
                    'message': "What's your expected selling price?",
                    'next': 'details',
                    'validation': lambda x: bool(x.strip())
                },
                'details': {
                    'message': "Please provide key details about your property (e.g., size, bedrooms, amenities)",
                    'next': 'end',
                    'validation': lambda x: bool(x.strip())
                },
                'end': {
                    'message': "Great! I'll help you create your property listing. Would you like to proceed?",
                    'next': None
                }
            }
        }
        self.user_states = {}
        self.flow_timeout = 3  # 5 minutes timeout

    def start_flow(self, flow_type, user_id):
        """Start a new conversation flow"""
        if flow_type not in self.flows:
            return "I apologize, but that conversation type isn't available."
            
        self.user_states[user_id] = {
            'flow': flow_type,
            'state': 'start',
            'data': {},
            'last_update': datetime.now()
        }
        return self.flows[flow_type]['start']['message']

    def get_current_flow_state(self, user_id):
        """Get the current state of user's conversation flow"""
        return self.user_states.get(user_id)

    def reset_flow(self, user_id):
        """Reset the conversation flow for a user"""
        if user_id in self.user_states:
            del self.user_states[user_id]

    def get_next_response(self, user_id, user_input):
        """Process user input and get next response"""
        try:
            if user_id not in self.user_states:
                return None

            # Check for timeout
            if self._check_timeout(user_id):
                return "Our conversation timed out. Would you like to start again?"

            # Get current flow and state
            current_flow = self.flows[self.user_states[user_id]['flow']]
            current_state = self.user_states[user_id]['state']
            
            # Validate input if validation function exists
            if 'validation' in current_flow[current_state]:
                if not current_flow[current_state]['validation'](user_input):
                    return f"I'm sorry, but I need a valid {current_state}. {current_flow[current_state]['message']}"

            # Store user's response
            self.user_states[user_id]['data'][current_state] = user_input
            
            # Update timestamp
            self.user_states[user_id]['last_update'] = datetime.now()

            # Get next state
            next_state = current_flow[current_state]['next']
            
            # Check if flow is complete
            if next_state is None:
                flow_data = self.user_states[user_id]['data']
                self.reset_flow(user_id)
                return self._generate_summary(flow_data, self.user_states[user_id]['flow'])

            # Update state and return next message
            self.user_states[user_id]['state'] = next_state
            return current_flow[next_state]['message']

        except Exception as e:
            logger.error(f"Error in flow progression: {str(e)}")
            self.reset_flow(user_id)
            return "I encountered an error. Would you like to start over?"

    def _check_timeout(self, user_id):
        """Check if the current flow has timed out"""
        if user_id in self.user_states:
            last_update = self.user_states[user_id].get('last_update')
            if last_update and (datetime.now() - last_update).seconds > self.flow_timeout:
                self.reset_flow(user_id)
                return True
        return False

    def _generate_summary(self, flow_data, flow_type):
        """Generate a summary of the conversation flow"""
        if flow_type == 'buying':
            return (
                f"Great! I'll look for {flow_data.get('start', 'properties')} "
                f"in {flow_data.get('location', 'your preferred area')} "
                f"within your budget of {flow_data.get('budget', 'specified range')}. "
                f"Requirements: {flow_data.get('requirements', 'None specified')}. "
                "I'll show you matching properties shortly."
            )
        elif flow_type == 'selling':
            return (
                f"Perfect! I'll help list your {flow_data.get('start', 'property')} "
                f"located in {flow_data.get('location', 'specified area')} "
                f"with an asking price of {flow_data.get('price', 'specified amount')}. "
                f"Details: {flow_data.get('details', 'None provided')}. "
                "Would you like to review your listing before publishing?"
            )
        return "Thank you for providing the information. How else can I help you?"

    def handle_interruption(self, user_id, user_input):
        """Handle user interruptions in the flow"""
        interrupt_commands = {'cancel', 'stop', 'quit', 'exit', 'restart', 'new'}
        if user_input.lower() in interrupt_commands:
            self.reset_flow(user_id)
            return "I've cancelled the current process. How else can I help you?"
        return None
def initialize_bot():
    """Initialize the bot"""
    try:
        # Configure logging
        logging.config.dictConfig(LOGGING_CONFIG)
        logger = logging.getLogger(__name__)
        
        # Initialize bot
        bot = NextopsonSupportBot()
        logger.info("Bot initialized successfully")
        return bot
    except Exception as e:
        # Fallback logging configuration if the dictConfig fails
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('nextopson_bot.log')
            ]
        )
        logger = logging.getLogger(__name__)
        logger.error(f"Bot initialization error: {str(e)}")
        return NextopsonSupportBot()


# Initialize bot when module is loaded
try:
    bot = initialize_bot()
except Exception as e:
    logging.error(f"Failed to initialize bot: {str(e)}")