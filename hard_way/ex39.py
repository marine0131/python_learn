states_short={
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

capitals = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

capitals['NY']='New York'
capitals['OR']='Portland'

print('-'*10)

print('please input a state (eg. California):')
state = input('> ').capitalize()
flag = True
while(flag):
    if state in states_short:
        print('its capital is %r' %capitals[states_short[state]])
    else:
        print('the state you input does not exist!')
    print('input state again or exit (input exit)')
    state=input('> ').capitalize()
    if state=='Exit':
        flag=False

print('have fun!')
    
    
