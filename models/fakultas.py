# from odoo import api, fields, models, tools

# class OpenFakultas(models.Model):
#     _name = "open.fakultas"
#     _description = "Fakultas"

#     name = fields.Char(string="Nama Fakultas", required="True")
#     prodi_ids = fields.One2many('open.programstudi', 'fakultas_id', string="Program Studi")

# class OpenProgramStudi(models.Model):
#     _name = "open.programstudi"
#     _description = "Program Studi"

#     name = fields.Char(string="Nama Program Studi", required=True)
#     fakultas_id = fields.Many2one('open.fakultas', string="Fakultas", required=True)