from odoo import api, fields, models, tools

class OpenMataKuliah(models.Model):
    _name = 'open.matakuliah'
    _description = "Mata Kuliah"

    name            = fields.Char(string="Mata Kuliah", required=True)
    sks             = fields.Integer(string="SKS")
    active          = fields.Boolean(string="Aktif", default=True)
    dosen_id        = fields.Many2one('open.dosen', string="Dosen")
    student_id      = fields.One2many('fits.student','matakuliah_id', string="Mahasiswa")