import streamlit as st
st.set_page_config(
    page_title="AI College Assistant",
    page_icon="🎓",
    layout="wide"
)
st.title("🎓 AI College Assistant")
st.write("Your smart assistant for college information and study support.")
st.sidebar.title("📚 College Assistant")
menu = st.sidebar.selectbox(
    "Choose an option",
    [
        "🏠 Home",
        "💬 AI Chat",
        "📚 Subjects",
        "📅 Timetable",
        "🏫 College Information"
    ]
)
if menu == "🏠 Home":
    st.header("Welcome to AI College Assistant 👋")
    st.write("""
    This application helps college students with:
    • Subject information
    • Study questions
    • Assignment support
    • College information
    • Timetable
    • AI-style chatting
    """)
    st.success("Select an option from the sidebar to get started!")
elif menu == "📚 Subjects":
    st.header("📚 Subjects")
    subjects = [
        "DBMS",
        "Data Structures",
        "Python",
        "Java",
        "Discrete Mathematics",
        "Computer Organization",
        "Digital Logic"
    ]
    subject = st.selectbox("Select your subject", subjects)
    st.info(f"You selected: {subject}")
    if subject == "DBMS":
        st.write("Topics: SQL, Normalization, Transactions, Indexing, B+ Trees")
    elif subject == "Data Structures":
        st.write("Topics: Arrays, Linked Lists, Stacks, Queues, Trees, Graphs")
    elif subject == "Python":
        st.write("Topics: Variables, Functions, Lists, Dictionaries, OOP, Streamlit")
    elif subject == "Java":
        st.write("Topics: Classes, Objects, Inheritance, Polymorphism, Exception Handling")
    elif subject == "Discrete Mathematics":
        st.write("Topics: Logic, Relations, Functions, Graph Theory, Groups")
    elif subject == "Computer Organization":
        st.write("Topics: CPU, Memory, Registers, ALU, Instruction Cycle")
    elif subject == "Digital Logic":
        st.write("Topics: Boolean Algebra, Logic Gates, K-Maps, Flip-Flops")
elif menu == "📅 Timetable":
    st.header("📅 College Timetable")
    timetable = {
        "Monday": "DBMS | Python | Mathematics",
        "Tuesday": "Java | Data Structures | Digital Logic",
        "Wednesday": "Python | DBMS | Computer Organization",
        "Thursday": "Mathematics | Java | Data Structures",
        "Friday": "Digital Logic | DBMS | Python"
    }
    for day, subjects in timetable.items():
        st.write(f"**{day}:** {subjects}")
elif menu == "🏫 College Information":
    st.header("🏫 College Information")
    st.write("### College Details")
    st.write("**College Name:** My College")
    st.write("**Department:** Computer Science / Information Technology")
    st.write("**Working Hours:** 9:00 AM - 4:00 PM")
    st.write("**Library:** 9:00 AM - 5:00 PM")
    st.write("### Important Contacts")
    st.write("📞 College Office: 1234567890")
    st.write("📧 Email: college@example.com")
elif menu == "💬 AI Chat":
    st.header("💬 AI College Assistant")
    st.write("Ask me a college-related question!")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    user_input = st.chat_input("Ask your question...")
    if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        with st.chat_message("user"):
            st.write(user_input)
        question = user_input.lower()
        if "dbms" in question:
            answer = "DBMS stands for Database Management System. It is used to store, manage and retrieve data efficiently."
        elif "python" in question:
            answer = "Python is a high-level programming language known for its simple syntax and wide range of applications."
        elif "java" in question:
            answer = "Java is an object-oriented programming language used to build desktop, web and enterprise applications."
        elif "exam" in question:
            answer = "For exams, make a study plan, revise important topics and practice previous questions."
        elif "assignment" in question:
            answer = "For assignments, first understand the question, prepare the answer and organize it with headings and examples."
        elif "attendance" in question:
            answer = "You can check your attendance through your college attendance portal or contact your department office."
        elif "library" in question:
            answer = "The library is generally used for textbooks, reference books, journals and study resources."
        else:
            answer = (
                "I'm your AI College Assistant. "
                "I can help with subjects, exams, assignments, "
                "college information and study-related questions."
            )
        with st.chat_message("assistant"):
            st.write(answer)
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()