from flask import Flask, render_template


main=Flask(__name__)


@main.route('/')
def funccome():
    return render_template('den.html')

@main.route('/home')
def home():
    return render_template('den.html')

@main.route('/photo')
def photo():
    return render_template('p24.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/new1')
def new1():
    return render_template('new 1.html')

@main.route('/new2')
def new2():
    return render_template('new 2.html')

@main.route('/new3')
def new3():
    return render_template('new 3.html')

@main.route('/new4')
def new4():
    return render_template('new 4.html')

@main.route('/new5')
def new5():
    return render_template('new 5.html')

@main.route('/new6')
def new6():
    return render_template('new 6.html')

@main.route('/new7')
def new7():
    return render_template('new 7.html')

@main.route('/p23')
def p23():
    return render_template('new 1.html')

@main.route('/p22')
def p22():
    return render_template('new 11.html')

@main.route('/p24')
def p24():
    return render_template('p24.html')

@main.route('/n11')
def n11():
    return render_template('new 11.html')

@main.route('/n12')
def n12():
    return render_template('new 12.html')

@main.route('/n13')
def n13():
    return render_template('new 13.html')

@main.route('/n14')
def n14():
    return render_template('new 14.html')

@main.route('/n15')
def n15():
    return render_template('new 15.html')

if __name__ =="__main__":
    main.run(debug=True)
