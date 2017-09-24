from flask import url_for, redirect, abort, flash, session, render_template, request
from flask_login import current_user, login_required

from app.lists_mod import forms
from forms import ItemForm
from app import models
from ..models import ListsItems
from . import lists_mod
from app import shoppers

@lists_mod.route('/dashboard',methods=['GET','POST'])
@login_required
def list_items():
 listitems=ListsItems.query.all()
 return render_template('dashboard/dashboard.html',listitems=listitems,title='ShoppingList') 
 
@lists_mod.route('/dashboard/add',methods=['GET','POST']) 
@login_required 
def add_item(): 
 add_item=True
 form=ItemForm()
 if request.method=='POST':
  try:
   if form.validate():
    Iname=form.name.data
    Description=form.description.data	
    item=ListsItems(Iname,Description)
    shoppers.session.add(item)
    shoppers.session.commit()
    flash('Successfully added item')
  except:
    flash('Already exists')
  return redirect(url_for('lists_mod.list_items')) 
 return render_template('dashboard/add.html', action="Add",
                           add_item=add_item, form=form,
                           title="Add Item")
						   

@lists_mod.route('/dashboard/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_item(id):
    add_item=False	

    item = ListsItems.query.get_or_404(id)
    form = ItemForm(obj=item)
    if form.validate():
        item.name=form.name.data
        item.description=form.description.data
        shoppers.session.commit()
        flash('Successfully edited')
        return redirect(url_for('lists_mod.list_items'))
  
    form.description.data = item.description
    form.name.data = item.name
 
    return render_template('dashboard/add.html', action="Edit",\
                            add_item=add_item, form=form,\
							item=item, title="Edit Item")
						   
@lists_mod.route('/dashboard/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_item(id):
 item = ListsItems.query.get_or_404(id)
 shoppers.session.delete(item)
 shoppers.session.commit()
 flash('Deleted Item')
 return redirect(url_for('lists_mod.list_items'))
 return render_template(title="Deleted Item")
 