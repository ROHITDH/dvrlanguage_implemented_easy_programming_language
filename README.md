//////////////////////////////////1//////////////////////////////////////////

basic arithmetic	:  + ,- ,* ,/

power				:  ^

floor division 		:  //

approx division 	:  ///

modulus				: %

--> [arithmetic expression may include parenthesis
     follows BODMAS rule]


//////////////////////////////////2//////////////////////////////////////////

variables : 
			SYNTAX
			------
			for assignment:
			1]	va identifier_name = value
			2]	directly writing 
				   identifier_name = value
			
			for access:
			1]  directly writing identifier_name
			
			
			-> identifier_name for declaring should not contain :
					"capital letters" 
					"special symbols"
					"digits"
					"blank spaces"
					"built- in keywards"
					"'_' (underscore) as starting letter"
					
			-> '_' (underscore) can be added in_between
			
			
			

constants : 
			SYNTAX
			------
			for assignment
			1]  co identifier_name = value
			
			for access:
			1] directly writing identifier_name
			
			-> identifier_name should not contain :
					"small letters" 
					"special symbols"
					"digits"
					"blank spaces"
			        "'_' (underscore) as starting letter"
					
			-> '_' (underscore) can be added in_between
			
			
			

--> multiple assignment can be done in same statement
    expression/assignment_1 ; expression/assignment_1; expression/assignment_1;
	
//////////////////////////////////3////////////////////////////////////////////

comparision :
			SYNTAX
			-------
				> 	: greater than
				<	: less than
				>=	: greater than
				<=  : less than
				==  : is equal
				!=  : is not equal
			
			result of / LHS and RHS side must be a int/floating point number

////////////////////////////////4//////////////////////////////////////////////

logical		:
			SYNTAX
				or  - or opereator
				ad  - and operator
				nt  - not operator - urinary operator ex: NT 1 results in 0
				
			result of / LHS and RHS side must be a int/floating point number										      
				

/////////////////////////////////5/////////////////////////////////////////////

if-tn statement:
			SYNTAX
			------
			for single line expression:
				if expression tn expression
						
		    for multi-line expression:
				if expression tn; expr_1 ; expr_2 ; expr 3 ;..............;end
				
				
			--> here, expr_1,expr_2...... may once again include "if statement" 
			    i.e nested if
			
			--> Constant assignment is only once, changing constant value gives
      			error	
			
			--> while writing program in file, ';' or writing in next line is acceptable
			
/////////////////////////////////6/////////////////////////////////////////////			
if-tn-el statements:
			SYNTAX
			------
			for single line expression:
				if expression tn expression el expression
						
		    for multi-line expression:
				if expression tn; expr_1 ; expr_2 ;...; el; expr_1 ; expr_2 ;...;end
				
			--> while writing program in file, ';' or writing in next line is acceptable
				
			--> here, expr_1,expr_2...... may once again include any nested condinational 
			    statements
			
			--> while writing program in file, ';' or writing in next line is acceptable

/////////////////////////////////7/////////////////////////////////////////////
				
for loop syntax:
	syntax:
		single line:
			fr variable_name = start_value to end_value sp step_value tn expression
	
		multi-line:
			fr variable_name = start_value to end_value sp step_value tn;exp1;exp2;exp3;end
			
	--> sp is optional, default  sp = 1
	--> end_value is included
	--> example: 	res = 0
					fr i = 1 to 5 tn res = res + i
					
					above example results in 15.
					
	--> SP can be negative too
		example:	res = 0
					fr i = 5 to 1 sp -1 tn res = res + i
					
					above example too results in 15.
					
	--> If SP is used in wrong sence as like shown below, 	
					res = 0
					fr i = 5 to 1 sp 1 tn res = res + i
					
					above example results in res = 0 itself and [] will be returned.
					
	--> Even the floating point values can be used in loop
	    example:	res = 0
					fr a = 2.3 to 7.2 sp 1.2 tn res = res + a
					
					above example results in res = 23.5
					It's because
					value of a (at each step)   end_value
					2.3 						<= 7.2  TRUE
					2.3 + 1.2 = 3.5 			<= 7.2  TRUE
					3.5 + 1.2 = 4.7				<= 7.2  TRUE
					4.7 + 1.2 = 5.9				<= 7.2  TRUE
					5.9 + 1.2 = 7.1				<= 7.2  TRUE
					
					7.1 + 1.2 = 8.3				<= 7.2  FALSE
					
					so the res = 2.3 + 3.5 + 4.7 + 5.9 + 7.1 = 23.5
	--> Ex: multi-line:
			fr a=1 to 10 sp 3 tn;b=b+a;c=c+a+2;end
	
	--> while writing program in file, ';' or writing in next line is acceptable

///////////////////////////////////////8/////////////////////////////////////////				
					
while loop 
		syntax
		------
		for single line expression:
				wl expression tn expression
				
				--> Example:
						a=0
						wl a<10 tn a=a+1
						
						will returns a=10
				
				--> 	a = 20
					    wl a<20 tn a=a+1
						above example return [] empty list.
						
		for multi-line expression:
				wl expression tn; expr_1 ; expr_2 ;...;end
				
			--> here, expr_1,expr_2...... may once again include any nested condinational 
			    statements
				--> Example:
						a=0
						wl a<10 tn;a=a+1;pt(a);end
	
	    
			--> 	a = 20
					wl a<20 tn;a=a+1;end
						above example doesn't return or do anything
									
/////////////////////////////////////////9/////////////////////////////////////		
	

Function:
			1] syntax:
				normal function:
					*) fn function_name (function_parameter(s)) -> function body/expressions 
					
				anonymous function:
					*) variable_name = fn (function_parameter(s)) -> function body/expressions

				
				multiline function with or without return:
				
		fn function_name(function_parameter(s));fn_line1;fn_line2;....;ret value/variable;end
				Ex: 
				fn mul(a,b);c=a*b;ret c;end;
				
			2] example:
					*)  fn mul(a,b) -> a^b
					    mul(3,2)
					    6
					
					*)  add = fn (a,b,c)->a+b+c
					    add(1,2,3)
					    6

		--> passing less/more arguments than required gives error
		
		--> If constant(s) is/are used inside function body/expressions it will going to take constant value
			Ex: co A = 10
				my_fun = fn (a,b,c)->a+b+c+A
				my_fun(1,2,3)
				16
		--> scope of variables used inside function is bonded inside function only. 
		
		--> If undifined variable/constants are used inside function body/expressions, function
			will be created but, function call results in error
			Ex: my_fun = fn (a,b,c)->a+b+c+A
				my_fun(1,2,3)
				'ERROR'
		
		--> Assigning of function to a Constant results in error
			Ex: co A=10
				A = fn (a,b,c)->a+b+c results in error
		
		--> Passing constants as arguments to function results in error
			Ex: co A = 20
				my_fun = fn (A,b,c)->A+b+c results in error
		--> One function variable can be assigned to another variable
			Ex: a=my_fun
		

		--> by using ret, multiple values can be returned by returning list.
			Ex:
			
			fn my_fun2(a,b,c);d=a+b;e=b+c;f=[d,e];ret f;end
			value=my_fun2(4,6,8)
				value is equal to [10,14]


/////////////////////////////////////////10//////////////////////////////////////

String:
		1] syntax:
		    "string"
		2] string concatenation:
			"string" + "string"
		3] string multiplication:
			"string" * value
		4] string assignment:
			variable_name = "string"
		5] string can be used inside function body/expressions
		
		6] string indexing:
		   character of a string at any index can be obtained by string.index_no
		   Ex: my_string = "dvr_lang"
			   my_srting.2 will return 'r'
			   my_srting.3 will return '_'
			   my_srting.6 will return 'n' ......etc

		7] string formatting :
		     \n - new line
			 \t - 1 tab space
			 \" - double quote
			 \\ - back slash
			 
//////////////////////////////////////////11////////////////////////////////////		

List:
		1] syntax:
		   a = [list elements sep by comma]
		   ex: a=[1,2,3,4]
		2] Accessing elements:
			obtained by list_name.index_no
			Ex: a=[1.1,2,3.5,4]
					a.0 = 1.1
					a.1 = 2
					a.2 = 3.5............etc
		    This will only return the element specified by it's index
			supports negative indexing.
			
		3] element poping from list:
			syntax: pop(list_name,index_no)
			Ex: a=[1,2,3,4,5]
				pop(a,3) returns 4
				and a will be assigned to [1,2,3,5]
		   
		   returns and removes the element specified by it's index
		   
		4] deleting elements of list:
			syntax:
			list_name - index_no
			
			Ex:
			a=[1,2,3,4]
			a-2 will make a=[1,2,4] and returns a
		
		5]  extending element(s) to list:
			--> adding single element:
					syntax: 
						1] list_name + value_to_append
						
					Ex: a=[1,2,3,4]
						a+5
					now a is equal to [1,2,3,4,5] and it returns it.
			--> extending elements of  a list to another list:
					syntax: list_name_1 + list_name_2
					
			These 2 methods will return and assign the newly created list.
			
			--> extend(list_name_1,list_name_2)
				will extend the elements but doesn't return anything.
				
//////////////////////////////////////////12///////////////////////////////////

break,continue statement:
          fr i=1 to 10 tn;if i==2 tn;con;end;pt(i);if i==7 tn;brk;end;end;
		  will going print:
			1
			3
			4
			5
			6
			7
			
		syntax: brk   	-- break
				con		-- continue
		 
//////////////////////////////////////////13//////////////////////////////////

return statement:
	syntax:
		ret value
		
		can be used inside function
		
		function may call other function or nested function call.

////////////////////////////////////////////14////////////////////////////////

pi = 3.141592653589793 is a inbuilt constant value.

INBUILT FUNCTIONS:

--> 1.	pt()
			use to print something on console
			Ex: pt("hai")
			
	2.	ptr()
			if assigned to variable/constant, it returns
			else prints on console.
			Ex: a = ptr("hai")
	3.	inp()
			use to get any input
			Ex: a=inp()
	4.  inpi()
			use to get only integer value
			Ex: a=inpi()
	5.  len()
			to find length of list
			Ex: a=[1,2,3,4]
			    len(a)
	6.  to check the type use
		IS_NUM()
		IS_STR()
		IS_LT()
		IS_FN()
		
		Ex: a=[1,2,3,4]
		    IS_LT(a) gives 1 i.e True
					
////////////////////////////////////////////////////////////////////////////////////////

KEYWARDS

	'va',
	'co',
	'ad',
	'or',
	'nt' , 
	'if',
	'tn',
	'ef',
	'el',
    'fr',
	'to',
	'sp',
	'wl',
    'fn',
	'end',
	'ret',
	'con',
	'brk'

	None
	FALSE
	TRUE

	pi
	pt
	ptr	
	inp
	inpi
	clr
	cls

	IS_NUM
	IS_STR
	IS_LT
	IS_FN

	pop
	extend
	len
	run


///////////////////////////////////////////////////////////////////////////////////////
				
PROGRAM FILE  AND HOW TO RUN A PROGRAM FILE??

--> program can be written in "any_file_name.txt" format by following the above all syntax
--> No any indentation has to be followed

--> 		SYNTAX
			------
			
			run("file_name.txt")
			
			Ex: run("my_program.txt")
			
			[txt is a file extension for a text file, used by a variety of text editors.]
			
			
--> program files can be imported in another file by including run("file_name.txt") at the 
    brginning.
	
	
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------	
------------------------here are some examples---------------------------------------------------
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------	


# no need to follow identation, but if followed better to read.
# here are some useful functions

# 1. function to find even/odd number
fn even_odd(a)
    if a%2 == 0 tn
        pt("Number is even")
    el 
        pt("Number is odd")
    end
end

even_odd(22)

# 2. function to find factorial of a number
fn factorial(a)
	res = 1
	
	fr i=a to 1 sp -1 tn
	    res = res * i
	end
    
	ret res	
end

factorial(3)

#this above function can also be written like this in 1 line, but not good method
#fn factorial(a);res = 1;fr i=a to 1 sp -1 tn;res = res * i;end;ret res;end	


# 3. function to print fibonacci series
fn fibonacci(a)
    x=0;y=1;pt(x);pt(y)
    fr i=2 to a-1 tn
        z=x+y;pt(z)
        x=y;y=z
    end
end

fibonacci(7)

# 4. function to check prime number
fn is_prime(n)
    f=0
	m=n/2
	fr i=2 to m tn
	    if n%i==0 tn
		    pt("number is not prime")
			f=1
			brk
		end
	end
	if f==0 tn
	    pt("number is prime")
	end
end	

is_prime(23)




---------------------------------------------------------------------------------------------
--> in order to import one file in other file:
	for example,
		let one file name be "one.txt"
		and other file name be "two.txt"
		
	in "two.txt" file the other file can be imported by writing 
		run("one.txt")
		than we can directly access the functions in one.txt


---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------


--> while writing program file, make sure to end any loops or conditional statements
	using 'end' keyward
	
--> contibute for the functions or collections of function file called 'module'
	 module creators, 
		each function name should contain
		module_name at the beggining followed by function name.
		Ex: 
			fn math_lcm_of_2(n1,n2)
				i=1
				fr i=1 to i<=n1 ad i<=n2 tn
					if n1%i==0 ad n2%i==0 tn
						gcd=i
					end
				end
				lcm = (n1*n2)/gcd
				pt("LCM is : ");pt(lcm)
			end
			    
		So that it won't collides the functiona and remains unique.
		
		
		
		
		
		
THANK_YOU
----------
dvrblacktech



