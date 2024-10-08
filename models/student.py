from odoo import api, fields, models, tools

class OpenStudent(models.Model):
    _name = 'fits.student'

    name            = fields.Char(string="Name")
    tempat_lahir    = fields.Char(string="Tempat Lahir")
    tgl_awal_kuliah = fields.Date(string="Tgl Awal Kuliah")
    no_ijazah       = fields.Char(string="No Ijazah")
    nem             = fields.Char(string="Nem")
    tgl_masuk       = fields.Date(string="Tgl Masuk")
    agama           = fields.Selection([('islam', 'Islam'),('kristen', 'Kristen'),('katolik', 'Katolik'),('hindu', 'Hindu'),('budha', 'Budha'),('konghucu', 'Konghucu')], string="Agama")
    jurusan_id      = fields.Many2one('open.jurusan', string="Jurusan SMA")
    pendidikan_ids  = fields.One2many('history.pendidikan', 'student_id', string="History Pendidikan")
    tinggal_student_ids = fields.One2many('tinggal.student', 'student_id', string="Tempat Tinggal Student")
    pengalaman_ids  = fields.One2many('open.pengalaman', 'student_id', string="Pengalaman Mahasiswa")
    matakuliah_id   = fields.Many2one('open.matakuliah', string="Mata Kuliah")

class OpenHistoryPendidikan(models.Model):
    _name = 'history.pendidikan'
    _description = "History Pendidikan"

    student_id = fields.Many2one('fits.student', string="Student")
    name       = fields.Char(string="Nama Sekolah")
    alamat     = fields.Char(string="Alamat Sekolah")
    keterangan = fields.Char(string="Keterangan")

class OpenJenisTinggal(models.Model):
    _name = 'jenis.tinggal'
    _description = "Jenis Tempat Tinggal"

    name            = fields.Char(string="Jenis Tempat Tinggal")
    keterangan      = fields.Char(string="Keterangan")


class OpenTinggalStudent(models.Model):
    _name = 'tinggal.student'
    _rec_name = "jenis_tinggal_id"

    student_id          = fields.Many2one('fits.student', string="Student")
    jenis_tinggal_id    = fields.Many2one('jenis.tinggal', string="Jenis Tinggal")
    alamat              = fields.Char(string="Alamat")

class OpenJurusan(models.Model):
    _name = 'open.jurusan'
    _description = "Jurusan"

    name            = fields.Char(string="Nama Jurusan")

class OpenPengalaman(models.Model):
    _name = 'open.pengalaman'
    _description = "Pengalaman Mahasiswa"

    student_id          = fields.Many2one('fits.student', string="Student")
    jenis_pengalaman_id = fields.Many2one('open.jenis.pengalaman', string="Jenis Pengalaman")
    tahun               = fields.Selection([('2019', '2019'), ('2020', '2020'), ('2021', '2021'),('2022', '2022'), ('2023', '2023'), ('2024', '2024')], string="Tahun")

class OpenJenisPengalaman(models.Model):
    _name = 'open.jenis.pengalaman'

    name    = fields.Char(string="Nama Pengalaman / Prestasi")
    keterangan = fields.Text(string="Keterangan")