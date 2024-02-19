extroverted_introverted = []
sensing_intuitive = []
thinking_feeling = []
judging_perceptive = []
mbti = []


def get_mbti_questions(question):
    mbti_questions = []

    mbti_questions.append("A. expend energy, enjoy groups\t\t\tB. conserve energy, enjoy one-on-one")
    mbti_questions.append("A. Interpret literally\t\t\tB. look for meaning and possibilities")
    mbti_questions.append("A. logical, thinking, questioning\t\t\tB. empathetic feeling, accommodating")
    mbti_questions.append("A. organized, orderly\t\t\tB. flexible, adaptable")
    mbti_questions.append("A. more outgoing, think out loud\t\t\tB. more reserved, think to yourself")
    mbti_questions.append("A. practical, realistic, experimental\t\t\tB. imaginative, innovative, theoretical")
    mbti_questions.append("A. candid, straight forward, frank\t\t\tB. tactful, kind encouraging")
    mbti_questions.append("A. plan, scheduled\t\t\tB. unplanned, spontaneous")
    mbti_questions.append("A. seek many tasks, public activities, interaction with others\t\t\t"
                          "B. seek private, solitary activities with quiet to concentrate")
    mbti_questions.append("A. standard, usual, conventional\t\t\tB. different, novel, unique")
    mbti_questions.append("A. firm, tend to criticize, hold the line\t\t\tB. gentle, tend to appreciate, conciliate")
    mbti_questions.append("A. regulated, structured\t\t\tB. easy-going, live and let live!")
    mbti_questions.append("A. external, communicative, express yourself\t\t\tB. internal, reticent, keep to yourself")
    mbti_questions.append("A. focus on here-and-now\t\t\tB. look to the future, global perspective, 'big picture'")
    mbti_questions.append("A. tough-minded, just\t\t\tB. tender-hearted, merciful")
    mbti_questions.append("A. preparation, plan ahead\t\t\tB. go with the flow, adapt as you go")
    mbti_questions.append("A. active, initiate\t\t\tB. reflective, deliberate")
    mbti_questions.append("A. facts, things, what is\t\t\tB. ideas, dreams, what could be, philosophical")
    mbti_questions.append("A. matter of fact, issue-oriented\t\t\tB. sensitive, people-oriented, compassionate")
    mbti_questions.append("A. control, govern\t\t\tB. latitude, freedom")

    return mbti_questions[question]


def display_questions():
    print()
    for number in range(20):
        print(get_mbti_questions(number))
        answer = input().upper()
        print()

        while answer != "A" and answer != "B":
            print("Expected A or B as Response\nI know this is an error, please retry again\n")
            print(get_mbti_questions(number))
            answer = input().upper()
            print()

        if (number + 1) == 1 or (number + 1) == 5 or (number + 1) == 9 or (number + 1) == 13 or (number + 1) == 17:
            extroverted_introverted.append(answer)
        if (number + 1) == 2 or (number + 1) == 6 or (number + 1) == 10 or (number + 1) == 14 or (number + 1) == 18:
            sensing_intuitive.append(answer)
        if (number + 1) == 3 or (number + 1) == 7 or (number + 1) == 11 or (number + 1) == 15 or (number + 1) == 19:
            thinking_feeling.append(answer)
        if (number + 1) == 4 or (number + 1) == 8 or (number + 1) == 12 or (number + 1) == 16 or (number + 1) == 20:
            judging_perceptive.append(answer)


def extroverted_vs_introverted():
    no_of_a = 0
    no_of_b = 0
    count = 0

    for answers in extroverted_introverted:
        if answers == "A":
            new_text = get_mbti_questions(count).split("\t")[0]
            print(new_text)
            no_of_a += 1
        else:
            new_text = get_mbti_questions(count).split("			")[1]
            print(new_text)
            no_of_b += 1

        count += 4

    print(f"Number of A selected: {no_of_a}")
    print(f"Number of B selected: {no_of_b}\n")

    if no_of_a > no_of_b:
        mbti.append("E")
    else:
        mbti.append("I")


def sensing_vs_intuitive():
    no_of_a = 0
    no_of_b = 0
    count = 1

    for answers in sensing_intuitive:
        if answers == "A":
            new_text = get_mbti_questions(count).split("\t")[0]
            print(new_text)
            no_of_a += 1
        else:
            new_text = get_mbti_questions(count).split("			")[1]
            print(new_text)
            no_of_b += 1

        count += 4

    print(f"Number of A selected: {no_of_a}")
    print(f"Number of B selected: {no_of_b}\n")

    if no_of_a > no_of_b:
        mbti.append("S")
    else:
        mbti.append("N")


def thinking_vs_feeling():
    no_of_a = 0
    no_of_b = 0
    count = 2

    for answers in thinking_feeling:
        if answers == "A":
            new_text = get_mbti_questions(count).split("\t")[0]
            print(new_text)
            no_of_a += 1
        else:
            new_text = get_mbti_questions(count).split("			")[1]
            print(new_text)
            no_of_b += 1

        count += 4

    print(f"Number of A selected: {no_of_a}")
    print(f"Number of B selected: {no_of_b}\n")

    if no_of_a > no_of_b:
        mbti.append("T")
    else:
        mbti.append("F")


def judging_vs_perceptive():
    no_of_a = 0
    no_of_b = 0
    count = 3

    for answers in judging_perceptive:
        if answers == "A":
            new_text = get_mbti_questions(count).split("\t")[0]
            print(new_text)
            no_of_a += 1
        else:
            new_text = get_mbti_questions(count).split("			")[1]
            print(new_text)
            no_of_b += 1

        count += 4

    print(f"Number of A selected: {no_of_a}")
    print(f"Number of B selected: {no_of_b}\n")

    if no_of_a > no_of_b:
        mbti.append("J")
    else:
        mbti.append("P")


def display_mbti():
    extroverted_vs_introverted()
    sensing_vs_intuitive()
    thinking_vs_feeling()
    judging_vs_perceptive()

    mbti_type = ''.join(mbti)

    match mbti_type:
        case "INFP":
            print("""INFP
      Healer
      The Thoughtful Idealist (MBTI)
      The Mediator (16Personalities)


The INFP Personality Type
    INFPs are imaginative idealists, guided by their own core values and beliefs. To a Healer,
    possibilities are paramount the realism of the moment is only of passing concern. They see
    potential for a better future, and pursue truth and meaning with their own individual flair.

    INFPs are sensitive, caring, and compassionate, and are deeply concerned with the personal
    growth of themselves and others. Individualistic and nonjudgmental, INFPs believe that each
    person must find their own path. They enjoy spending time exploring their own ideas and
    values, and are gently encouraging to others to do the same. INFPs are creative and often
    artistic they enjoy finding new outlets for self-expression.

What does INFP stand for?
    INFP is one of the sixteen personality types created by Katharine Briggs and Isabel Myers,
    creators of the Myers-Briggs Type Indicator (MBTI®). INFP stands for Introversion,
    iNtuition, Feeling, and Perceiving, which are four core personality traits based on the
    work of psychologist C.G. Jung.

    Each of the four letters of the INFP code signifies a key personality trait of this type.
    INFPs are energized by time alone (Introverted), focus on ideas and concepts rather than
    facts and details (iNtuitive), make decisions based on feelings and values (Feeling), and
    prefer to be spontaneous and flexible rather than planned and organized (Perceiving).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "INTJ":
            print("""INTJ
      Mastermind
      The Conceptual Planner (MBTI)
      The Architect (16Personalities)


The INTJ Personality Type
    INTJs are analytical problem-solvers, eager to improve systems and processes with their innovative
    ideas. They have a talent for seeing possibilities for improvement, whether at work, at home, or
    in themselves.

    Often intellectual, INTJs enjoy logical reasoning and complex problem-solving. They approach life
    by analyzing the theory behind what they see, and are typically focused inward, on their own
    thoughtful study of the world around them. INTJs are drawn to logical systems and are much less
    comfortable with the unpredictable nature of other people and their emotions. They are typically
    independent and selective about their relationships, preferring to associate with people who they
    find intellectually stimulating.

What does INTJ stand for?
    INTJ is one of the sixteen personality types created by Katharine Briggs and Isabel Myers, creators
    of the Myers-Briggs Type Indicator (MBTI®). INTJ stands for Introverted, iNtuitive, Thinking,
    Judging, which are four core personality traits based on the work of psychologist C.G. Jung.

    Each of the four letters of the INTJ code signifies a key personality trait of this type. INTJs are
    energized by time alone (Introverted), focus on ideas and concepts rather than facts and details
    (iNtuitive), make decisions based on logic and reason (Thinking) and prefer to be planned and
    organized rather than spontaneous and flexible (Judging).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "INFJ":
            print("""INFJ
      Counselor
      The Insightful Visionary (MBTI)
      The Advocate (16Personalities)


The INFJ Personality Type
    INFJs are thoughtful nurturers with a strong sense of personal integrity and a drive to help others
    realize their potential. Creative and dedicated, they have a talent for helping others with original
    solutions to their personal challenges.

    The Counselor has a unique ability to intuit others' emotions and motivations, and will often know
    how someone else is feeling before that person knows it himself. They trust their insights about
    others and have strong faith in their ability to read people. Although they are sensitive, they are
    also reserved; the INFJ is a private sort, and is selective about sharing intimate thoughts
    and feelings.

What does INFJ stand for?
    INFJ is one of the sixteen personality types created by Katharine Briggs and Isabel Myers, creators
    of the Myers-Briggs Type Indicator (MBTI®). Each of the four letters of the INFJ code signifies a
    key personality trait of this type. The letters INFJ stand for the following dimensions of
    personality, based on the work of psychologist C.G. Jung:

        * Introverted: INFJs are energized by time alone
        * iNtuitive: INFJs focus on ideas and concepts rather than facts and details
        * Feeling: INFJs make decisions based on feelings and values
        * Judging: INFJs prefer to be planned and organized rather than spontaneous and flexible


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "INTP":
            print("""INTP
      Architect
      The Objective Analyst (MBTI)
      The Logician (16Personalities)


The INTP Personality Type
    INTPs are philosophical innovators, fascinated by logical analysis, systems, and design. They are
    preoccupied with theory, and search for the universal law behind everything they see. They want to
    understand the unifying themes of life, in all their complexity.

    INTPs are detached, analytical observers who can seem oblivious to the world around them because
    they are so deeply absorbed in thought. They spend much of their time in their own heads: exploring
    concepts, making connections, and seeking understanding of how things work. To the Architect, life
    is an ongoing inquiry into the mysteries of the universe.

What does INTP stand for?
    INTP is one of the sixteen personality types created by Katharine Briggs and Isabel Myers, creators of
    the Myers-Briggs Type Indicator (MBTI®). INTP stands for Introverted, iNtuitive, Thinking, Perceiving,
    which are four core personality traits based on the work of psychologist C.G. Jung.

    The INTP type describes a person who is energized by time alone (Introverted), who focuses on ideas and
    concepts rather than facts and details (iNtuitive), who makes decisions based on logic and reason
    (Thinking) and who prefers to be spontaneous and flexible rather than planned and organized (Perceiving).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ENFP":
            print("""ENFP
      Champion
      The Imaginative Motivator (MBTI)
      The Campaigner (16Personalities)


The ENFP Personality Type
    ENFPs are people-centered creators with a focus on possibilities and a contagious enthusiasm for
    new ideas, people and activities. Energetic, warm, and passionate, ENFPs love to help other
    people explore their creative potential.

    ENFPs are typically agile and expressive communicators, using their wit, humor, and mastery of
    language to create engaging stories. Imaginative and original, ENFPs often have a strong artistic
    side. They are drawn to art because of its ability to express inventive ideas and create a deeper
    understanding of human experience.

What does ENFP stand for?
    ENFP is one of the sixteen personality types created by Katharine Briggs and Isabel Myers, creators
    of the Myers-Briggs Type Indicator (MBTI®). ENFP stands for Extraversion, iNtuition, Feeling, and
    Perceiving, which are four core personality traits based on the work of psychologist C.G. Jung.

    Each of the four letters of the ENFP code signifies a key personality trait of this type. ENFPs are
    energized by time spent with others (Extraverted), focus on ideas and concepts rather than facts and
    details (iNtuitive), make decisions based on feelings and values (Feeling), and prefer to be
    spontaneous and flexible rather than planned and organized (Perceiving).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ENTJ":
            print("""ENTJ
      Commander
      The Natural Leader (MBTI)
      The Commander (16Personalities)


The ENTJ Personality Type
    ENTJs are strategic leaders, motivated to organize change. They are quick to see inefficiency and
    conceptualize new solutions, and enjoy developing long-range plans to accomplish their vision.
    They excel at logical reasoning and are usually articulate and quick-witted.

    ENTJs are analytical and objective, and like bringing order to the world around them. When there
    are flaws in a system, the ENTJ sees them, and enjoys the process of discovering and implementing a
    better way. ENTJs are assertive and enjoy taking charge they see their role as that of leader and
    manager, organizing people and processes to achieve their goals.

What does ENTJ stand for?
    ENTJ is an acronym used to describe one of the sixteen personality types created by Katharine Briggs
    and Isabel Myers. It stands for Extraverted, iNtuitive, Thinking, Judging. ENTJ indicates a person who
    is energized by time spent with others (Extraverted), who focuses on ideas and concepts rather than
    facts and details (iNtuitive), who makes decisions based on logic and reason (Thinking) and who prefers
    to be planned and organized rather than spontaneous and flexible (Judging).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ENTP":
            print("""ENTP
      Visionary
      The Debater (16Personalities)


The ENTP Personality Type
    ENTPs are inspired innovators, motivated to find new solutions to intellectually challenging problems.
    They are curious and clever, and seek to comprehend the people, systems, and principles that surround
    them. Open-minded and unconventional, Visionaries want to analyze, understand, and influence other people.

    ENTPs enjoy playing with ideas and especially like to banter with others. They use their quick wit and
    command of language to keep the upper hand with other people, often cheerfully poking fun at their habits
    and eccentricities. While the ENTP enjoys challenging others, in the end they are usually happy to live and
    let live. They are rarely judgmental, but they may have little patience for people who can't keep up.

What does ENTP stand for?
    ENTP is an acronym used to describe one of the sixteen personality types created by Katharine Briggs and
    Isabel Myers. It stands for Extraverted, iNtuitive, Thinking, Perceiving. ENTP indicates a person who is
    energized by time spent with others (Extraverted), who focuses on ideas and concepts rather than facts
    and details (iNtuitive), who makes decisions based on logic and reason (Thinking) and who prefers to be
    spontaneous and flexible rather than planned and organized (Perceiving).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ENFJ":
            print("""ENFJ
      Teacher
      The Protagonist (16Personalities)


The ENFJ Personality Type
    ENFJs are idealist organizers, driven to implement their vision of what is best for humanity. They often
    act as catalysts for human growth because of their ability to see potential in other people and their
    charisma in persuading others to their ideas. They are focused on values and vision, and are passionate
    about the possibilities for people.

    ENFJs are typically energetic and driven, and often have a lot on their plates. They are tuned into the
    needs of others and acutely aware of human suffering however, they also tend to be optimistic and
    forward-thinking, intuitively seeing opportunity for improvement. The ENFJ is ambitious, but their
    ambition is not self-serving: rather, they feel personally responsible for making the world a better place.

What does ENFJ stand for?
    ENFJ is an acronym used to describe one of the sixteen personality types created by Katharine Briggs and
    Isabel Myers. It stands for Extraverted, iNtuitive, Feeling, Judging. ENFJ indicates a person who is
    energized by time spent with others (Extraverted), who focuses on ideas and concepts rather than facts
    and details (iNtuitive), who makes decisions based on feelings and values (Feeling) and who prefers to
    be planned and organized rather than spontaneous and flexible (Judging).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ISFJ":
            print("""ISFJ
      Protector
      The Defender (16Personalities)


The ISFJ Personality Type
    ISFJs are industrious caretakers, loyal to traditions and organizations. They are practical, compassionate,
    and caring, and are motivated to provide for others and protect them from the perils of life.

    ISFJs are conventional and grounded, and enjoy contributing to established structures of society. They are
    steady and committed workers with a deep sense of responsibility to others. They focus on fulfilling their
    duties, particularly when they are taking care of the needs of other people. They want others to know that
    they are reliable and can be trusted to do what is expected of them. They are conscientious and methodical,
    and persist until the job is done.

What does ISFJ stand for?
    ISFJ is an acronym used to describe one of the sixteen personality types created by Katharine Briggs and
    Isabel Myers. It stands for Introverted, Sensing, Feeling, Judging. ISFJ indicates a person who is energized
    by time spent alone (Introverted), who focuses on facts and details rather than ideas and concepts (Sensing),
    who makes decisions based on feelings and values (Feeling) and who prefers to be planned and organized rather
    than spontaneous and flexible (Judging).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ISFP":
            print("""ISFP
      Composer
      The Adventurer (16Personalities)


The ISFP Personality Type
    ISFPs are gentle caretakers who live in the present moment and enjoy their surroundings with cheerful,
    low-key enthusiasm. They are flexible and spontaneous, and like to go with the flow to enjoy what life
    has to offer. ISFPs are quiet and unassuming, and may be hard to get to know. However, to those who
    know them well, the ISFP is warm and friendly, eager to share in life's many experiences.

    ISFPs have a strong aesthetic sense and seek out beauty in their surroundings. They are attuned to
    sensory experience, and often have a natural talent for the arts. ISFPs especially excel at manipulating
    objects, and may wield creative tools like paintbrushes and sculptor's knives with great mastery.

What does ISFP stand for?
    ISFP is an acronym used to describe one of the sixteen personality types created by Katharine Briggs and
    Isabel Myers. It stands for Introverted, Sensing, Feeling, Perceiving. ISFP indicates a person who is
    energized by time spent alone (Introverted), who focuses on facts and details rather than ideas and
    concepts (Sensing), who makes decisions based on feelings and values (Feeling) and who prefers to be
    spontaneous and flexible rather than planned and organized (Perceiving).


 For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
                           """)
        case "ISTJ":
            print("""ISTJ
      Inspector
      The Logistician (16Personalities)


The ISTJ Personality Type
    ISTJs are responsible organizers, driven to create and enforce order within systems and institutions.
    They are neat and orderly, inside and out, and tend to have a procedure for everything they do.
    Reliable and dutiful, ISTJs want to uphold tradition and follow regulations.

    ISTJs are steady, productive contributors. Although they are Introverted, ISTJs are rarely isolated
    typical ISTJs know just where they belong in life, and want to understand how they can participate in
    established organizations and systems. They concern themselves with maintaining the social order and
    making sure that standards are met.

What does ISTJ stand for?
    ISTJ is an acronym used to describe one of the sixteen personality types created by Katharine Briggs and
    Isabel Myers. It stands for Introverted, Sensing, Thinking, Judging. ISTJ indicates a person who is
    energized by time spent alone (Introverted), who focuses on facts and details rather than ideas and
    concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be
    planned and organized rather than spontaneous and flexible (Judging).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ISTP":
            print("""ISTP
      Craftsman
      The Virtuoso (16Personalities)


The ISTP Personality Type
    ISTPs are observant artisans with an understanding of mechanics and an interest in troubleshooting.
    They approach their environments with a flexible logic, looking for practical solutions to the
    problems at hand. They are independent and adaptable, and typically interact with the world around
    them in a self-directed, spontaneous manner.

    ISTPs are attentive to details and responsive to the demands of the world around them. Because of
    their astute sense of their environment, they are good at moving quickly and responding to
    emergencies. ISTPs are reserved, but not withdrawn: the ISTP enjoys taking action, and approaches
    the world with a keen appreciation for the physical and sensory experiences it has to offer.

What does ISTP stand for?
    ISTP is an acronym used to describe one of the sixteen personality types created by Katharine Briggs
    and Isabel Myers. It stands for Introverted, Sensing, Thinking, Perceiving. ISTP indicates a person
    who is energized by time spent alone (Introverted), who focuses on facts and details rather than ideas
    and concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be
    spontaneous and flexible rather than planned and organized (Perceiving).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ESFJ":
            print("""ESFJ
      Provider
      The Consul (16Personalities)


The ESFJ Personality Type
    ESFJs are conscientious helpers, sensitive to the needs of others and energetically dedicated to their
    responsibilities. They are highly attuned to their emotional environment and attentive to both the
    feelings of others and the perception others have of them. ESFJs like a sense of harmony and cooperation
    around them, and are eager to please and provide.

    ESFJs value loyalty and tradition, and usually make their family and friends their top priority. They
    are generous with their time, effort, and emotions. They often take on the concerns of others as if
    they were their own, and will attempt to put their significant organizational talents to use to bring
    order to other people's lives.

What does ESFJ stand for?
    ESFJ is an acronym used to describe one of the sixteen personality types created by Katharine Briggs and
    Isabel Myers. It stands for Extraverted, Sensing, Feeling, Judging. ESFJ indicates a person who is
    energized by time spent with others (Extraverted), who focuses on facts and details rather than ideas
    and concepts (Sensing), who makes decisions based on feelings and values (Feeling) and who prefers to be
    planned and organized rather than spontaneous and flexible (Judging).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ESFP":
            print("""ESFP
      Performer
      The Entertainer (16Personalities)


The ESFP Personality Type
    ESFPs are vivacious entertainers who charm and engage those around them. They are spontaneous, energetic,
    and fun-loving, and take pleasure in the things around them: food, clothes, nature, animals, and
    especially people.

    ESFPs are typically warm and talkative and have a contagious enthusiasm for life. They like to be in the
    middle of the action and the center of attention. They have a playful, open sense of humor, and like to
    draw out other people and help them have a good time.

What does ESFP stand for?
    ESFP is an acronym used to describe one of the sixteen personality types created by Katharine Briggs and
    Isabel Myers. It stands for Extraverted, Sensing, Feeling, Perceiving. ESFP indicates a person who is
    energized by time spent with others (Extraverted), who focuses on facts and details rather than ideas
    and concepts (Sensing), who makes decisions based on feelings and values (Feeling) and who prefers to be
    spontaneous and flexible rather than planned and organized (Perceiving).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ESTJ":
            print("""ESTJ
      Supervisor
      The Executive (16Personalities)


The ESTJ Personality Type
    ESTJs are hardworking traditionalists, eager to take charge in organizing projects and people.
    Orderly, rule-abiding, and conscientious, ESTJs like to get things done, and tend to go about
    projects in a systematic, methodical way.

    ESTJs are the consummate organizers, and want to bring structure to their surroundings. They
    value predictability and prefer things to proceed in a logical order. When they see a lack of
    organization, the ESTJ often takes the initiative to establish processes and guidelines, so that
    everyone knows what's expected.

What does ESTJ stand for?
    ESTJ is an acronym used to describe one of the sixteen personality types created by Katharine Briggs
    and Isabel Myers. It stands for Extraverted, Sensing, Thinking, Judging. ESTJ indicates a person who
    is energized by time spent with others (Extraverted), who focuses on facts and details rather than
    ideas and concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who
    prefers to be planned and organized rather than spontaneous and flexible (Judging).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
        case "ESTP":
            print("""ESTP
      Dynamo
      The Entrepreneur (16Personalities)


The ESTP Personality Type
    ESTPs are energetic thrill-seekers who are at their best when putting out fires, whether literal or
    metaphorical. They bring a sense of dynamic energy to their interactions with others and the world
    around them. They assess situations quickly and move adeptly to respond to immediate problems with
    practical solutions.

    Active and playful, ESTPs are often the life of the party and have a good sense of humor. They use
    their keen powers of observation to assess their audience and adapt quickly to keep interactions
    exciting. Although they typically appear very social, they are rarely sensitive the ESTP prefers to
    keep things fast-paced and silly rather than emotional or serious.

What does ESTP stand for?
    ESTP is an acronym used to describe one of the sixteen personality types created by Katharine Briggs
    and Isabel Myers. It stands for Extraverted, Sensing, Thinking, Perceiving. ESTP indicates a person
    who is energized by time spent with others (Extraverted), who focuses on facts and details rather
    than ideas and concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who
    prefers to be spontaneous and flexible rather than planned and organized (Perceiving).


For more information, visit https://www.truity.com/blog/page/16-personality-types-myers-briggs
""")
