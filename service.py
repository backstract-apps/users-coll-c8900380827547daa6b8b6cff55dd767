from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_student(db: Session):

    student_all = db.query(models.Student).order_by(models.Student.id).all()
    res = {
        'student_all': student_all,
    }
    return res

async def get_student_user_id(db: Session, user_id: int):

    student_one = db.query(models.Student).filter(models.Student.user_id == 'user_id').first()
    res = {
        'student_one': student_one,
    }
    return res

async def post_student(db: Session, raw_data: schemas.PostStudent):
    user_id:int = raw_data.user_id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password
    role:str = raw_data.role


    record_to_be_added = {'user_id': user_id, 'name': name, 'email': email, 'password': password, 'role': role}
    new_student = models.Student(**record_to_be_added)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    student_inserted_record = new_student
    res = {
        'student_inserted_record': student_inserted_record,
    }
    return res

async def put_student_user_id(db: Session, raw_data: schemas.PutStudentUserId):
    user_id:str = raw_data.user_id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password
    role:str = raw_data.role


    student_edited_record = db.query(models.Student).filter(models.Student.user_id == user_id).first()
    for key, value in {'user_id': user_id, 'name': name, 'email': email, 'password': password, 'role': role}.items():
          setattr(student_edited_record, key, value)
    db.commit()
    db.refresh(student_edited_record)
    student_edited_record = student_edited_record

    res = {
        'student_edited_record': student_edited_record,
    }
    return res

async def delete_student_user_id(db: Session, user_id: int):

    student_deleted = None
    record_to_delete = db.query(models.Student).filter(models.Student.user_id == user_id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        student_deleted = record_to_delete
    res = {
        'student_deleted': student_deleted,
    }
    return res

async def get_tasks(db: Session):

    tasks_all = db.query(models.Tasks).order_by(models.Tasks.id).all()
    res = {
        'tasks_all': tasks_all,
    }
    return res

async def get_tasks_id(db: Session, id: int):

    tasks_one = db.query(models.Tasks).filter(models.Tasks.id == 'id').first()
    res = {
        'tasks_one': tasks_one,
    }
    return res

async def post_tasks(db: Session, raw_data: schemas.PostTasks):
    id:str = raw_data.id
    title:str = raw_data.title
    description:str = raw_data.description
    status:str = raw_data.status
    priority:str = raw_data.priority


    record_to_be_added = {'id': id, 'title': title, 'description': description, 'status': status, 'priority': priority}
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    tasks_inserted_record = new_tasks
    res = {
        'tasks_inserted_record': tasks_inserted_record,
    }
    return res

async def put_tasks_id(db: Session, raw_data: schemas.PutTasksId):
    id:int = raw_data.id
    title:str = raw_data.title
    description:str = raw_data.description
    status:str = raw_data.status
    priority:str = raw_data.priority


    tasks_edited_record = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    for key, value in {'id': id, 'title': title, 'description': description, 'status': status, 'priority': priority}.items():
          setattr(tasks_edited_record, key, value)
    db.commit()
    db.refresh(tasks_edited_record)
    tasks_edited_record = tasks_edited_record

    res = {
        'tasks_edited_record': tasks_edited_record,
    }
    return res

async def delete_tasks_id(db: Session, id: int):

    tasks_deleted = None
    record_to_delete = db.query(models.Tasks).filter(models.Tasks.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tasks_deleted = record_to_delete
    res = {
        'tasks_deleted': tasks_deleted,
    }
    return res

