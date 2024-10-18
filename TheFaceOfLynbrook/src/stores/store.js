import {persistStore} from './persistStore'

const defaultState = "/"
export const state = persistStore("state", defaultState)

const defaultSuccess = false
export const success = persistStore("success", defaultSuccess)

const defaultImgFile = "gens/def.jpg"
export const genImgFile = persistStore("gen", defaultImgFile)

const numGensDefault = false
export const numGens = persistStore("numGens", 0)

const justGeneratedDefault = false
export const justGenerated = persistStore("justGen", justGeneratedDefault)

const lastGeneratedDefault = Date.now()
export const lastGenerated = persistStore("lastGen", justGeneratedDefault)

const defaultGanCallInProgress = false
export const ganCallInProgress = persistStore("ganCall", defaultGanCallInProgress)