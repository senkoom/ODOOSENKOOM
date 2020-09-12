
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError, AccessError
from odoo.modules.module import get_module_resource
class Journalier(models.Model):
    _name = 'journalier.journalier'  # Le nom du modèle
    _description = 'Module journalier'
    _rec_name = 'sequence_id'



    # Début déclaration des champs
    sequence_id = fields.Char('Séquence', readonly=True)
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_de_naissance = fields.Date(string='Date de naissance', required=True)
    numero_identification = fields.Char(string='Numéro Identification', required=True)
    genre = fields.Selection([('Femme', 'Femme'),
                              ('Homme', 'Homme'), ], string="Status", default='Femme')
    state = fields.Selection([('Occupé', 'Occupé'),
                              ('Libre', 'Libre'), ], string="Etat", default='Libre')


    # Fin déclaration des champs

    # Création du numéro de séquence
    @api.model
        def create(self, vals):
           seq = self.env['ir.sequence'].next_by_code('journalier.journalier') or '/'
           vals['sequence_id'] = seq
           return super(Journalier, self).create(vals)


    # Gestion des états (occupé/Libre) des journaliers
    @api.one
        def occupe_progressbar(self):
           self.write({'state': 'Occupé', })


    @api.one
        def libre_progressbar(self):
           self.write({'state': 'Libre'})


    # Gestion de la contrainte de numéro unique pour le numéro d'identification
    _sql_constraints = [
        ('id_unique', 'UNIQUE(numero_identification)', 'Ce numéro d\'identification existe déja dans notre base')]