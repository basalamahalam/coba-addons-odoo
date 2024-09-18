from odoo import api, fields, models, tools

class OpenDosen(models.Model):
    _name = 'open.dosen'
    _description = "Data Dosen"

    photo_filename  = fields.Char("Nama File Foto")
    name            = fields.Char(string="Nama Lengkap", required=True)
    nip             = fields.Char(string="NIP", required=True)
    email           = fields.Char(string="Email")
    phone           = fields.Char(string="Telepon")
    address         = fields.Text(string="Alamat")
    bidangkeahlian_id = fields.Many2one('open.bidangkeahlian', string="Bidang Keahlian")
    jabatan         = fields.Selection([
                        ('lektor', 'Lektor'),
                        ('profesor', 'Profesor'),
                        ('asisten', 'Asisten'),
                        ('lainnya', 'Lainnya'),
                    ], string="Jabatan")
    active          = fields.Boolean(string="Aktif", default=True)
    matakuliah_ids  = fields.One2many('open.matakuliah', 'dosen_id', string="Mata Kuliah")


class OpenBidangKeahlian(models.Model):
    _name = 'open.bidangkeahlian'
    _description = "Bidang Keahlian Dosen"

    name            = fields.Char(string="Bidang Keahlian", required=True) 

# class OpenBiodataDosen(models.Model):
#     _name = 'open.biodata.dosen'
#     _description = "Biodata Dosen"

#     fakultas_id = fields.Many2one('open.fakultas', string="Fakultas", required=True)
#     prodi_id = fields.Many2one('open.program.studi', string="Program Studi", required=True, domain="[('fakultas_id', '=', fakultas_id)]")

#     dosen_id = fields.Many2one('open.dosen', string="Dosen", required=True)