import pretty_midi

# pretty_midiオブジェクトを作ります
pm = pretty_midi.PrettyMIDI(resolution=960, initial_tempo=120)
#instrumentはトラックみたいなものです。
instrument = pretty_midi.Instrument(0)

note_number = pretty_midi.note_name_to_number('G4')
#noteはNoteOnEventとNoteOffEventに相当します。
note = pretty_midi.Note(velocity=100, pitch=note_number, start=0, end=1)
instrument.notes.append(note)
note_number = pretty_midi.note_name_to_number('G0')
note = pretty_midi.Note(velocity=100, pitch=note_number, start=2, end=3)
instrument.notes.append(note)



pm.instruments.append(instrument)
pm.write('test.mid') #midiファイルを書き込みます。