from .BaseDataModel import BaseDataModel
from .db_schemas import Project
from .enums.DatabaseEnum import DatabaseEnum

class ProjectModel(BaseDataModel):

    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DatabaseEnum.COLLECTION_PROJECT_NAME.value]

    async def create_project(self, project: Project):

        result = await self.collection.insert_one(project.dict())
        project._id = result.inserted_id

        return project
        
    async def get_project_or_create_one(self, project_id: str):

        record = await self.collection.find_one({
            "project_id": project_id
            })
        
        if record is None:
            # Create a new project
            new_project = Project(project_id=project_id)
            created_project = await self.create_project(project=new_project)

            return created_project
        
        return Project(**record) # Convert dict to Project model instance
    
    async def get_all_projects(self, page: int = 1, page_size: int = 10):

        # Count total number of documents
        total_documents = await self.collection.count_documents({})

        # Calculate total pages
        total_pages = total_documents // page_size
        if total_documents % page_size > 0:
            total_pages += 1

        cursor = self.collection.find().skip((page - 1) * page_size).limit(page_size)
        projects = []
        async for document in cursor:
            projects.append(
                Project(**document)
                )  # Convert dict to Project model instance
            
        return projects, total_pages