from scholarly import scholarly
import argparse

if __name__=="__main__":
	
	print("START")
	args=argparse.ArgumentParser()
	args.add_argument("--name",type=str,dest="name",default=None)
	args.add_argument("--year",type=int,dest="year",default=None)

	args=args.parse_args()
	
	authors=scholarly.search_author(args.name)
	author=next(authors)

	while True:
		print("------")
		print(author['name'], author['affiliation'])
		print("Is this the correct profile?")
		ans=input("Y or N?\n")
		if ans.strip()=="Y":
			break
		author=next(authors)

	author=scholarly.fill(author)


	print("*********************")
	print("Citations of {} ({}) 's publications for year {}".format(author['name'],author['affiliation'],args.year))


	pubIdx=1
	allPubsCitationIdx=1
	errors=[]

	for pub in author['publications']:
		# print(pub)
		scholarly.fill(pub)
		# print(pub)
		# try:
		thisPubCitationIdx=1
		print("{}\t {}\t {}.\t{}".format(pubIdx,"-","-",pub['bib']['title']))
		citations=scholarly.citedby(pub)
		for citation in citations:
			if citation['bib']['pub_year']==str(args.year):
				print("{}\t {}\t {}.\t{}".format(pubIdx,thisPubCitationIdx,allPubsCitationIdx,citation['bib']['title']))
				thisPubCitationIdx+=1
				allPubsCitationIdx+=1
		pubIdx+=1

		# except:
		# 	print("err")
		# 	errors.append(pub['bib']['title'])



	if len(errors)>0:
		print("There were errors in {} publications.".format(len(errors)))
		print(errors)






	print("END of Program")



