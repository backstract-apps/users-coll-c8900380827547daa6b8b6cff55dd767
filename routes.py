from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/student/')
async def get_student(db: Session = Depends(get_db)):
    try:
        return await service.get_student(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/student/user_id')
async def get_student_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_student_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/student/')
async def post_student(raw_data: schemas.PostStudent, db: Session = Depends(get_db)):
    try:
        return await service.post_student(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/student/user_id/')
async def put_student_user_id(raw_data: schemas.PutStudentUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_student_user_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/student/user_id')
async def delete_student_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_student_user_id(db, user_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/')
async def get_tasks(db: Session = Depends(get_db)):
    try:
        return await service.get_tasks(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/id')
async def get_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tasks/')
async def post_tasks(raw_data: schemas.PostTasks, db: Session = Depends(get_db)):
    try:
        return await service.post_tasks(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tasks/id/')
async def put_tasks_id(raw_data: schemas.PutTasksId, db: Session = Depends(get_db)):
    try:
        return await service.put_tasks_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tasks/id')
async def delete_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

