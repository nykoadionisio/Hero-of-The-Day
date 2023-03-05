import random

from flask import Flask, render_template
from summarize import summarize
from wikiscraper import scrape

app = Flask(__name__)

# Loading the data
muhammad_ali_prompt = """
born Cassius Marcellus Clay Jr.;[5] January 17, 1942 – June 3, 2016) was an American professional boxer and activist. Nicknamed "The Greatest", he is regarded as one of the most significant sports figures of the 20th century and is frequently ranked as the greatest heavyweight boxer of all time.[6][7][8] In 1999, he was named Sportsman of the Century by Sports Illustrated and the Sports Personality of the Century by the BBC.

Born and raised in Louisville, Kentucky, he began training as an amateur boxer at age 12. At 18, he won a gold medal in the light heavyweight division at the 1960 Summer Olympics and turned professional later that year. He became a Muslim after 1961. He won the world heavyweight championship, defeating Sonny Liston in a major upset on February 25, 1964, at age 22. During that year, he denounced his birth name as a "slave name" and formally changed his name to Muhammad Ali. In 1966, Ali refused to be drafted into the military owing to his religious beliefs and ethical opposition to the Vietnam War[9][10] and was found guilty of draft evasion and stripped of his boxing titles. He stayed out of prison while appealing the decision to the Supreme Court, where his conviction was overturned in 1971. He did not fight for nearly four years and lost a period of peak performance as an athlete.[11] Ali's actions as a conscientious objector to the Vietnam War made him an icon for the larger counterculture of the 1960s generation,[12][13] and he was a very high-profile figure of racial pride for African Americans during the civil rights movement and throughout his career.[9] As a Muslim, Ali was initially affiliated with Elijah Muhammad's Nation of Islam (NOI). He later disavowed the NOI, adhering to Sunni Islam.

He fought in several historic boxing matches, including his highly publicized fights with Sonny Liston, Joe Frazier (including the Fight of the Century, the biggest boxing event up until then),[14] the Thrilla in Manila, and his fight with George Foreman in The Rumble in the Jungle.[15][16] Ali thrived in the spotlight at a time when many boxers let their managers do the talking, and he became renowned for his provocative and outlandish persona.[17][18][19] He was famous for trash-talking, often free-styled with rhyme schemes and spoken word poetry incorporating elements of hip hop.[20][21][22] He often predicted in which round he would knock out his opponent.

Outside boxing, Ali attained success as a spoken word artist, releasing two studio albums: I Am the Greatest! (1963) and The Adventures of Ali and His Gang vs. Mr. Tooth Decay (1976). Both albums received Grammy Award nominations.[22] He also featured as an actor and writer, releasing two autobiographies. Ali retired from boxing in 1981 and focused on religion, philanthropy and activism. In 1984, he made public his diagnosis of Parkinson's syndrome, which some reports attributed to boxing-related injuries,[23] though he and his specialist physicians disputed this.[24] He remained an active public figure globally, but in his later years made fewer public appearances as his condition worsened, and he was cared for by his family.
"""
muhammad_a_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Muhammad_Ali_NYWTS.jpg/440px-Muhammad_Ali_NYWTS.jpg"


jesse_owens_prompt = """
James Cleveland "Jesse" Owens (September 12, 1913 – March 31, 1980) was an American track and field athlete who won four gold medals at the 1936 Olympic Games.[3]

Owens specialized in the sprints and the long jump and was recognized in his lifetime as "perhaps the greatest and most famous athlete in track and field history".[4] He set three world records and tied another, all in less than an hour, at the 1935 Big Ten track meet in Ann Arbor, Michigan—a feat that has never been equaled and has been called "the greatest 45 minutes ever in sport".[5]

He achieved international fame at the 1936 Summer Olympics in Berlin, Germany, by winning four gold medals: 100 meters, long jump, 200 meters, and 4 × 100-meter relay. He was the most successful athlete at the Games and, as a black American man, was credited with "single-handedly crushing Hitler's myth of Aryan supremacy".[6]

The Jesse Owens Award is USA Track and Field's highest accolade for the year's best track and field athlete. Owens was ranked by ESPN as the sixth greatest North American athlete of the 20th century and the highest-ranked in his sport. In 1999, he was on the six-man short-list for the BBC's Sports Personality of the Century.
"""
jesse_o_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Jesse_Owens_1936.jpg/440px-Jesse_Owens_1936.jpg"


august_wilson_promt = """
August Wilson (né Frederick August Kittel Jr.; April 27, 1945 – October 2, 2005) was an American playwright. He has been referred to as the "theater's poet of Black America".[1] He is best known for a series of ten plays, collectively called The Pittsburgh Cycle (or The Century Cycle), which chronicle the experiences and heritage of the African-American community in the 20th century. Plays in the series include Fences (1987) and The Piano Lesson (1990), both of which won the Pulitzer Prize for Drama, as well as Ma Rainey's Black Bottom (1984) and Joe Turner's Come and Gone (1988). In 2006, Wilson was inducted into the American Theater Hall of Fame.

His works delve into the African-American experience as well as examinations of the human condition. Other themes range from the systemic and historical exploitation of African Americans, as well as race relations, identity, migration, and racial discrimination. Viola Davis said that Wilson's writing "captures our humor, our vulnerabilities, our tragedies, our trauma. And he humanizes us. And he allows us to talk."[2] Since Wilson's death two of his plays have been adapted into films: Fences (2016) and Ma Rainey's Black Bottom (2020). Denzel Washington has shepherded the films and has vowed to continue Wilson's legacy by adapting the rest of his plays into films for a wider audience.[3] Washington said, "the greatest part of what's left of my career is making sure that August is taken care of".[4]

Wilson knew that he wanted to be a writer, but this created tension with his mother, who wanted him to become a lawyer. She forced him to leave the family home and he enlisted in the United States Army for a three-year stint in 1962, but he left after one year[clarify] and went back to working various odd jobs as a porter, short-order cook, gardener, and dishwasher.[citation needed]

Frederick August Kittel Jr. changed his name to August Wilson to honor his mother after his father's death in 1965. That same year, he discovered the blues as sung by Bessie Smith, and he bought a stolen typewriter for $10, which he often pawned when money was tight.[8] At 20, he decided he was a poet and submitted work to such magazines as Harper's.[5] He began to write in bars, the local cigar store, and cafes—longhand on table napkins and on yellow notepads, absorbing the voices and characters around him. He liked to write on cafe napkins because, he said, it freed him up and made him less self-conscious as a writer. He would then gather the notes and type them up at home.[5] Gifted with a talent for catching dialect and accents, Wilson had an "astonishing memory", which he put to full use during his career. He slowly learned not to censor the language he heard when incorporating it into his work.[8]
"""
august_w_img = "https://upload.wikimedia.org/wikipedia/en/f/fa/August_wilson.jpg"

prompts = {"Muhammad Ali": [muhammad_ali_prompt, muhammad_a_img],
           "Jesse Owens": [jesse_owens_prompt, jesse_o_img],
           "August Wilson": [august_wilson_promt, august_w_img]}


@app.route('/')
def index():
    # person = scrape()
    # person_prompt = person[0]
    # person_img = person[1]
    # output = summarize(person_prompt)
    random_person = random.choice(list(prompts.keys()))
    random_prompt = prompts[random_person][0]
    output = summarize(random_prompt)
    person_img = prompts[random_person][1]

    return render_template("index.html", name=random_person, id=output,
                           img_ad=person_img)


if "__name__" == "__main__":
    app.run(debug=True)
