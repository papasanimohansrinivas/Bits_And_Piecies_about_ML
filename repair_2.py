with  open("cs231.ipynb","r") as f:
	var =  f.read()
	f.close()

import json

dict_ =  json.loads(var)

num1=0
number=1

import ast

for i1 in  dict_['cells']:
	if i1['cell_type'] == "code":
		
		source_code =  i1['source']

		code = ''.join(source_code)

		roots  = ast.parse(code)

		names = sorted({node.id for node in ast.walk(roots) if type(node)==ast.Name})

		vras  = ["eip", "mlblr", "eip_in", "eip_out", "mlblr_in", "mlblr_out", "eip_list", "eip_dict"]
		import keyword
		names = [Keyword for Keyword in names if keyword.iskeyword(Keyword)==False]
		imp_words = ["len","type","list","range","enumerate","int","sqrt","object","imread","imresize","pdist","squareform", "imsave"]
		for vwords in imp_words:
			try:
				names.remove(vwords)
			except ValueError:
				pass
		assert len(vras)>=len(names)

		replacements = {}
		
		ss = vras[:len(names)]

		for a1,a2 in zip(names,ss):
			replacements[a1]=a2

		for no in ast.walk(roots):

			if type(no)==ast.Name :
				original =  no.__getattribute__('id')
				if original not in imp_words:

					arr1 = no.__dict__['id']
	
					no.__setattr__('id',replacements[original])

		import astunparse

		xp = astunparse.unparse(roots)

		xeq = ["np","plt"]

		for keq  in xeq:
			try:

				xp = xp.replace(keq,replacements[keq])
			except KeyError:
				pass
			
		
		i1['source']=xp
		print i1['source']
		number+=1

with open("modifiedcs231.ipynb","w") as fd:
	fd.write(json.dumps(dict_)) 
