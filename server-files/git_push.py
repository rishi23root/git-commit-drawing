# pip install PyGithub
import datetime
from github import Github

class git_use :
	def __init__(self,username,passwd):
		self.g = Github(username,passwd)
		self.user = self.g.get_user()

	def creating_repo(self,reponame):
		self.repo = self.user.create_repo(reponame)

	def select_repo(self,reponame) :
		self.repo = self.user.get_repo(reponame)


	def creating_file(self,filename,commit,data) :
		# fielname ,commit ,data to commit 
		self.repo.create_file(filename,commit,data)

	def updateing_file(self,filename,commit,updated_data):
		contents =self.repo.get_contents(filename)
		self.repo.update_file(contents.path,commit,updated_data,contents.sha)

	
	def total_commits(self):
		commitlen = 0
		try:
			for _ in self.repo.get_commits():
				commitlen += 1
		except :
			pass

		return commitlen

	def last_commit_date(self):
		for i in self.repo.get_commits():
			last_comment_date = self.repo.get_commit(i.sha).commit.committer.date.date()
			break

		return last_comment_date

	def readme_data(self) :
		data = f'''# This repo is for drawing on git commit\n### check out the real-repo for more info '''
		return data


def runner(username,passwd):
	# first login o git 
	git = git_use(username,passwd)
	# select repo of our need
	try:
		git.creating_repo('git-drawing')
		return
	except :
		git.select_repo('git-drawing')

	print('total on this repo are :',git.total_commits())

	# make first commit of the repo of readme.md and add data to it 
	if not git.total_commits():
		git.creating_file('README.md','UPLOADING readme.MD',git.readme_data())
		return

	# check if there is any commit today if yes then just update the file
	# here and condition is because it is one commit new repo is created
	if (git.total_commits() > 1 ) and (datetime.datetime.now().date() == git.last_commit_date()):
		git.updateing_file(f'{datetime.datetime.now().date()}.txt',f'commiting on {datetime.datetime.now()}',f'file data is date and time {datetime.datetime.now()} currenly git-commit count on this repo is {git.total_commits() + 1}')
	# else just create a new file
	else :
		git.creating_file(f'{datetime.datetime.now().date()}.txt',f'commiting on {datetime.datetime.now()}',f'file data is date and time {datetime.datetime.now()} currenly git-commit count on this repo is {git.total_commits() + 1}')

