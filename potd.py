from flask import Flask, render_template
from summarize import summarize

app = Flask(__name__)

# Loading the data
muhammad_ali_prompt = """
born Cassius Marcellus Clay Jr.;[5] January 17, 1942 – June 3, 2016) was an American professional boxer and activist. Nicknamed "The Greatest", he is regarded as one of the most significant sports figures of the 20th century and is frequently ranked as the greatest heavyweight boxer of all time.[6][7][8] In 1999, he was named Sportsman of the Century by Sports Illustrated and the Sports Personality of the Century by the BBC.

Born and raised in Louisville, Kentucky, he began training as an amateur boxer at age 12. At 18, he won a gold medal in the light heavyweight division at the 1960 Summer Olympics and turned professional later that year. He became a Muslim after 1961. He won the world heavyweight championship, defeating Sonny Liston in a major upset on February 25, 1964, at age 22. During that year, he denounced his birth name as a "slave name" and formally changed his name to Muhammad Ali. In 1966, Ali refused to be drafted into the military owing to his religious beliefs and ethical opposition to the Vietnam War[9][10] and was found guilty of draft evasion and stripped of his boxing titles. He stayed out of prison while appealing the decision to the Supreme Court, where his conviction was overturned in 1971. He did not fight for nearly four years and lost a period of peak performance as an athlete.[11] Ali's actions as a conscientious objector to the Vietnam War made him an icon for the larger counterculture of the 1960s generation,[12][13] and he was a very high-profile figure of racial pride for African Americans during the civil rights movement and throughout his career.[9] As a Muslim, Ali was initially affiliated with Elijah Muhammad's Nation of Islam (NOI). He later disavowed the NOI, adhering to Sunni Islam.

He fought in several historic boxing matches, including his highly publicized fights with Sonny Liston, Joe Frazier (including the Fight of the Century, the biggest boxing event up until then),[14] the Thrilla in Manila, and his fight with George Foreman in The Rumble in the Jungle.[15][16] Ali thrived in the spotlight at a time when many boxers let their managers do the talking, and he became renowned for his provocative and outlandish persona.[17][18][19] He was famous for trash-talking, often free-styled with rhyme schemes and spoken word poetry incorporating elements of hip hop.[20][21][22] He often predicted in which round he would knock out his opponent.

Outside boxing, Ali attained success as a spoken word artist, releasing two studio albums: I Am the Greatest! (1963) and The Adventures of Ali and His Gang vs. Mr. Tooth Decay (1976). Both albums received Grammy Award nominations.[22] He also featured as an actor and writer, releasing two autobiographies. Ali retired from boxing in 1981 and focused on religion, philanthropy and activism. In 1984, he made public his diagnosis of Parkinson's syndrome, which some reports attributed to boxing-related injuries,[23] though he and his specialist physicians disputed this.[24] He remained an active public figure globally, but in his later years made fewer public appearances as his condition worsened, and he was cared for by his family. 
"""


@app.route('/')
def index():
    output = summarize(muhammad_ali_prompt)
    return render_template("index.html", id=output)

if "__name__" == "__main__":
    app.run(debug=True)
