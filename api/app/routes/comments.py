from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.models.comments import Comment
from app.schemas.comments import CommentCreate, CommentUpdate, CommentResponse
from app.deps import get_db, get_current_user
from app.models.users import User

router = APIRouter(prefix="/comments", tags=["comments"])

@router.get("/", response_model=list[CommentResponse] | CommentResponse)
def get_comments(
    comment_id: int = Query(None),
    post_id: int = Query(None),
    user_id: int = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if comment_id:
        comment = db.query(Comment).get(comment_id)
        if not comment:
            raise HTTPException(status_code=404, detail="Comentario no encontrado")
        return comment
    
    offset = (page - 1) * limit
    
    query = db.query(Comment)
    
    if user_id:
        query = query.filter(Comment.id_usuario == user_id)

    if post_id:
        query = query.filter(Comment.id_publicacion == post_id)

    return query.offset(offset).limit(limit).all()

@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_comment = Comment(
        comentario=comment.comentario,
        id_publicacion=comment.id_publicacion,
        id_usuario=current_user.id,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@router.put("/{comment_id}", response_model=CommentResponse)
def update_comment(comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_comment = db.query(Comment).get(comment_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    if db_comment.id_usuario != current_user.id:
        raise HTTPException(status_code=403, detail="No puedes editar este comentario")

    for key, value in comment.dict(exclude_unset=True).items():
        setattr(db_comment, key, value)

    db.commit()
    db.refresh(db_comment)
    return db_comment


@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_comment = db.query(Comment).get(comment_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    if db_comment.id_usuario != current_user.id:
        raise HTTPException(status_code=403, detail="No puedes eliminar este comentario")

    db.delete(db_comment)
    db.commit()
    return {"message": "Comentario eliminado"}